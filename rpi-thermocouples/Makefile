CXX := g++
CFLAGS = -std=c++11 -Wall

.PHONY: all
all: example_main

example_main: example_main.cpp
	$(CXX) $(CFLAGS) $^ -o $@ -lwiringPi

.PHONY: all
clean:
	rm -f example_main
