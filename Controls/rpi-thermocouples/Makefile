CXX := g++
CFLAGS = -std=c++11 -Wall -march=native

# Debugging
CFLAGS += -g
# Release
CFLAGS += -O3

.PHONY: all
all: example_main

example_main: example_main.cpp
	$(CXX) $(CFLAGS) $^ -o $@ -lwiringPi

.PHONY: all
clean:
	rm -f example_main
