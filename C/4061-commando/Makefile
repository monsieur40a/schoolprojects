CFLAGS = -std=gnu99 -Wall -g
CC = gcc $(CFLAGS)

commando: commando.o cmd.o cmdcol.o util.o commando.h
	$(CC) -o $@ $^ # $@ becomes commando, $^ is all dependecies

commando.o: commando.c commando.h
	$(CC) -c $^ # $< is the first dependency only

cmd.o: cmd.c commando.h
	$(CC) -c $^

cmdcol.o: cmdcol.c commando.h
	$(CC) -c $^

util.o: util.c commando.h
	$(CC) -c $^

test : test-functions test-commando

test-functions : test_functions
	@printf "Tests for correctness of functions\n"
	./test_functions
	@printf "\n"
	@printf "Valgrind with function tests\n"
	valgrind ./test_functions

test-commando : commando
	@printf "Tests for correctness of commando program\n"
	chmod u+x test_commando.sh standardize_pids
	./test_commando.sh

test_utils.o : test_utils.c test_utils.h
	$(CC) -c $^

test_functions.o : test_functions.c commando.h test_utils.h
	$(CC) -c $^

test_functions : test_functions.o cmd.o cmdcol.o test_utils.o
	$(CC) -o $@ $^

clean-tests :
	rm -f test_functions test-data/*.tmp

clean:
	rm -f commando  *.o

# fixes two small issues with tests that may cause correct code to
# fail because test data has slightly altered during transfers
fix-tests:
	touch test-data/stuff/empty
	chmod a=rw test-data/stuff/*
	chmod a=rwx test-data/stuff/table.sh
	chmod 777 test-data/table.sh
