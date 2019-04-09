#include "commando.h"

int main(int argc, char *argv[]){
    setvbuf(stdout, NULL, _IONBF, 0); // Turn off output buffering

    // Check for echo argument
    int echo = 0;
    if (argc > 1){
        if (strncmp(argv[1], "--echo", 6) == 0 ){
            echo = 1;
        }
    }
    // If environment exists
    if (getenv("COMMANDO_ECHO")){
        // Get value
        char *echoenv = getenv("COMMANDO_ECHO");
        // Check value for equivalence to "1"
        if (strncmp(echoenv, "1", 1) == 0){
            echo = 1;
        }
    }

    // Initialize command struct full of cmds and size attributes
    cmdcol_t *commands = malloc(sizeof(cmdcol_t));
    if(commands == NULL){
        perror("Unable to malloc commands, failure.");
        exit(1);
    }
    commands->size = 0;

    char buffer[MAX_LINE]; // Initialize buffer for fgets
    int numtokens; // Initialize numtokens for parse_into_tokens
    char *tokens[MAX_CMDS]; // **argv equivalent for storing tokens

    while(1){
        printf("@> ");

        // Get full line, length of MAX_LINE from stdin, put into buffer
        if (fgets(buffer, MAX_LINE, stdin) == NULL) {
            printf("\nEnd of input\n");
            break;
        }

        if(echo){
            printf("%s", buffer); // Echo input if desired
        }

        parse_into_tokens(buffer, tokens, &numtokens); // Parse buffer into tokens for execvp execution
        if (numtokens != 0) { // If more than just newline, Enter hit, in buffer
            if (strncmp(tokens[0], "help", 4) == 0){
                printf("COMMANDO COMMANDS\n");
                printf("help               : show this message\n");
                printf("exit               : exit the program\n");
                printf("list               : list all jobs that have been started giving information on each\n");
                printf("pause nanos secs   : pause for the given number of nanseconds and seconds\n");
                printf("output-for int     : print the output for given job number\n");
                printf("output-all         : print output for all jobs\n");
                printf("wait-for int       : wait until the given job number finishes\n");
                printf("wait-all           : wait for all jobs to finish\n");
                printf("command arg1 ...   : non-built-in is run as a job\n");
            } else if (strncmp(tokens[0], "exit", 4) == 0){
                break;
            } else if (strncmp(tokens[0], "list", 4) == 0){
                cmdcol_print(commands);
            } else if (strncmp(tokens[0], "pause", 5) == 0){
                if (numtokens == 3){ // If "pause" token, and two more tokens exist
                    pause_for(atoi(tokens[1]), atoi(tokens[2])); // send to util pause_for function
                } else { // Else not enough tokens for pause command
                    printf("Not enough arguments to pause\n");
                }
            } else if (strncmp(tokens[0], "output-for", strlen("output-for") + 1) == 0){
                if (numtokens == 2){ // Check for "output-for" check for one addtl token
                    int jobnumber = atoi(tokens[1]); // Get job number
                    if (commands->size - 1 >= jobnumber){ // Make sure it's in range
                        printf("@<<< Output for %s[#%d] (%d bytes):\n",
                            commands->cmd[jobnumber]->name, commands->cmd[jobnumber]->pid, commands->cmd[jobnumber]->output_size);
                        printf("----------------------------------------\n");
                        cmd_print_output(commands->cmd[jobnumber]); // Print cmd->output
                        printf("----------------------------------------\n");
                    } else {
                        printf("Job number not found\n");
                    }
                } else {
                    printf("Not enough arguments to output-for\n");
                }
            } else if (strncmp(tokens[0], "output-all", strlen("output-all") + 1) == 0){
                for (int i = 0, size = commands->size; i < size; i++){ // Same logic as output-for, looped through size
                    printf("@<<< Output for %s[#%d] (%d bytes):\n",
                        commands->cmd[i]->name, commands->cmd[i]->pid, commands->cmd[i]->output_size);
                    printf("----------------------------------------\n");
                    cmd_print_output(commands->cmd[i]);
                    printf("----------------------------------------\n");
                }
            } else if (strncmp(tokens[0], "wait-for", strlen("wait-for") + 1) == 0){
                if (numtokens == 2){ // Check number tokens
                    int jobnumber = atoi(tokens[1]); // Get jobnumber
                    if (commands->size - 1 >= jobnumber){ // Make sure it's in range
                        cmd_update_state(commands->cmd[jobnumber], DOBLOCK); // Send block to wait
                    } else {
                        printf("Job number not found\n");
                    }
                } else {
                    printf("Not enough arguments to wait-for\n");
                }
            } else if (strncmp(tokens[0], "wait-all", strlen("wait-all") + 1) == 0){
                cmdcol_update_state(commands, DOBLOCK); // Send block via cmdcol for all cmds
            } else {
                cmd_t *cmd = cmd_new(tokens);
                cmd_start(cmd);
                cmdcol_add(commands, cmd);
            }
        }
        cmdcol_update_state(commands, NOBLOCK); // Update state, nonblocking after if else block

    }
    cmdcol_freeall(commands); // free all cmds from heap
    free(commands); // free cmdcol commands
}
