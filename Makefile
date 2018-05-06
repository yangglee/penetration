all:test
test:test.o
	clang -o test test.o
test.o:test.c
	clang -g -c test.c
.PHONY:all
clean:
	-rm -rf *.o test
