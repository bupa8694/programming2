# Makefile for MA4
all:
	g++ -std=c++11 -c -fPIC integer.cpp -o integer.o
	g++ -std=c++11 -shared -o libinteger.so  integer.o	
clean:
	rm -fr *.o *.so __pycache__