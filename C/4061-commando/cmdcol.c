#include "commando.h"

void cmdcol_add(cmdcol_t *col, cmd_t *cmd){
    if(col->size + 1 == MAX_CMDS){ // Error if too many commands
        perror("Error, too many commands, can't add");
        return;
    }
    col->cmd[col->size] = cmd; // Set to current idx, increase size
    col->size = col->size + 1;
}

void cmdcol_print(cmdcol_t *col){
    printf("JOB  #PID      STAT   STR_STAT OUTB COMMAND\n"); // Format output
    for(int i = 0, size = col->size; i < size; i++){
        printf("%-4d #%-8d %4d %10s %4d ",
            i, col->cmd[i]->pid, col->cmd[i]->status,
            col->cmd[i]->str_status,
            col->cmd[i]->output_size);

        int j = 0;
        while(col->cmd[i]->argv[j] != NULL){ // Print token args
            printf("%-s ", col->cmd[i]->argv[j]);
            j++;
        }
        printf("\n");
    }
}


void cmdcol_update_state(cmdcol_t *col, int nohang){
    for(int i = 0, size = col->size; i < size; i++){
        cmd_update_state(col->cmd[i], nohang);
    }
}

void cmdcol_freeall(cmdcol_t *col){
    for(int i = 0, size = col->size; i < size; i++){
        cmd_free(col->cmd[i]);
    }
}
