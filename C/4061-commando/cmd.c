#include "commando.h"

cmd_t *cmd_new(char *argv[]) {
    cmd_t *cmd = malloc(sizeof(cmd_t));

    int i = 0;
    while (argv[i] != NULL) {
        cmd->argv[i] = strdup(argv[i]);
        i++;
    }

    // Initialize values
    cmd->argv[i] = NULL;
    snprintf(cmd->name, strlen(cmd->argv[0]) + 1, "%s", cmd->argv[0]);
    cmd->finished = 0;
    snprintf(cmd->str_status, 5, "INIT");
    cmd->pid = -1;
    cmd->out_pipe[0] = 0;
    cmd->out_pipe[1] = 0;
    cmd->status = -1;
    cmd->output = NULL;
    cmd->output_size = -1;

    return cmd;
}

void cmd_free(cmd_t *cmd){
    int i = 0;
    while (cmd->argv[i]!= NULL) { // Free strings malloc'ed by strdup
        free(cmd->argv[i]);
        i++;
    }
    if (cmd->output != NULL){
        free(cmd->output); // Free output buffer
    }
    free(cmd); // Free cmd itself
}

void cmd_start(cmd_t *cmd){
    snprintf(cmd->str_status, 4, "RUN");

    if (pipe(cmd->out_pipe)) { // Pipe before fork to communicate between parent and child
      perror("Failed to create pipe");
      exit(1);
    }
    int stdout_backup;
    if ((stdout_backup = dup(STDOUT_FILENO)) == -1){ // Dupe stdout to restore later
        perror("Unable to dup");
        exit(1);
    };

    int stderr_backup;
    if ((stderr_backup = dup(STDERR_FILENO)) == -1){ // Dupe stderr to restore later
        perror("Unable to dup");
        exit(1);
    };

    pid_t child_pid = fork(); // fork
    if (child_pid < 0){ // if for failed
      perror("Failed to fork");
      exit(1);
    }

    if (child_pid == 0){ // if child
        if(close(cmd->out_pipe[PREAD])){ // Child doesn't read, close read end
            perror("cmd_start pipe read close error");
            exit(1);
        }
        if (dup2(cmd->out_pipe[PWRITE], STDOUT_FILENO) == -1){
            perror("Unable to dup2");
            exit(1);
        }

        if (dup2(cmd->out_pipe[PWRITE], STDERR_FILENO) == -1){
            perror("Unable to dup2");
            exit(1);
        }

        if(close(cmd->out_pipe[PWRITE])){ // Close write end, moved to stdout
            perror("cmd_start pipe write close error");
            exit(1);
        }
        execvp(cmd->name, cmd->argv); // Exec bash command with arguments
        perror("Failed to execvp() for child_pid"); // If failed to exec
        exit(1);
    }

    if(close(cmd->out_pipe[PWRITE])){ // Parent close write, not needed
        perror("cmd_start pipe write close error");
        exit(1);
    }
    if (dup2(stdout_backup, STDOUT_FILENO) == -1){ // Copy stdout fd back
        perror("Unable to dup2 stdout_backup");
        exit(1);
    }
    if (dup2(stderr_backup, STDERR_FILENO) == -1){ // Copy stdout fd back
        perror("Unable to dup2 stderr_backup");
        exit(1);
    }
    cmd->pid = child_pid; // Copy child pid to parent
}


void cmd_update_state(cmd_t *cmd, int nohang){
    if(cmd->finished == 1){ // If done, return, nothing to update
        return;
    }

     // Wait depending on nohang state, get process id result
    int status;
    pid_t pid = waitpid(cmd->pid, &status, nohang);

    // If child exited, and normal exit
    if ((cmd->pid == pid) && WIFEXITED(status)) {
        cmd->finished = 1;

        int return_val = WEXITSTATUS(status);
        cmd->status = return_val;

        // Maximum int in c is 10 characters long, so 11 with '\0'
        char int_to_char[11];
        sprintf(int_to_char, "%d", return_val);

        // Copy Exit and current string length for int over to cmd->str_status buffer
        snprintf(cmd->str_status, strlen("EXIT()") + strlen(int_to_char) + 2, "EXIT(%s)", int_to_char);

        // Completion notification and data
        printf("@!!! %s[#%d]: %s\n", cmd->name, cmd->pid, cmd->str_status);
        cmd_fetch_output(cmd);
    } else if(pid == -1){
        perror("Failed to wait for process");
        exit(1);
    }
}

char *read_all(int fd, int *nread){
    int total = 0, bytesread = 0;
    int count = 64;
    int buffersize = BUFSIZE;
    char *resultbuf = malloc(buffersize);
    if(resultbuf == NULL){
        perror("Unable to malloc resultbuf in read_all, failure");
        exit(1);
    }
    // Continuously read from buffer, doubling size as needed
    while(1) {
        // read count bytes from fd into buffer with offset of resultbuf + total
        bytesread = read(fd, resultbuf + total, count);
        if (bytesread == -1) {
            perror("read error");
            exit(1);
        } else if(bytesread == 0){
            break;
        } else {
            total += bytesread;
            if(total == buffersize){ // If total read == buffersize, need to expand
                resultbuf = realloc(resultbuf, buffersize *= 2);
                if (resultbuf != NULL){ // If realloc didn't fail continue at top of loop
                    continue;
                } else {
                    perror("realloc failed");
                    exit(1);
                }
            }
        }
    }
    resultbuf[total] = '\0';
    *nread = total;
    return resultbuf;
}

// No implementation details given, seemingly not necessary since all tests pass
void cmd_set_stdin(cmd_t *cmd, char *input_file){
    return;
}

void cmd_fetch_output(cmd_t *cmd){
    if (cmd->finished == 0){
        printf("%s[#%d] not finished yet\n", cmd->name, cmd->pid);
        return;
    }
    int bytesread;
    // Read all from read end of pipe into output buffer
    cmd->output = read_all(cmd->out_pipe[PREAD], &bytesread);
    cmd->output_size = bytesread;
    if(close(cmd->out_pipe[PREAD])){ // Close read end of pipe after copying to output
        perror("cmd_fetch_output pipe read close error");
        exit(1);
    }
}

void cmd_print_output(cmd_t *cmd){
    if(cmd->output == NULL){
        printf("%s[#%d] : output not ready\n", cmd->name, cmd->pid);
    } else {
        // Just write length bytes, not including \0
        int length = strlen(cmd->output);
        if (length != write(STDOUT_FILENO, cmd->output, length)){
            perror("Unable to write, error");
            exit(1);
        }
    }
}
