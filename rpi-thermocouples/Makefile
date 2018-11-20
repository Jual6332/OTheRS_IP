CXX := g++
CFLAGS = -std=c++11 -Wall

.PHONY: all
all: thermocouple

thermocouple: thermocouple.cpp
	$(CXX) $(CFLAGS) $^ -o $@ -lwiringPi

.PHONY: all
clean:
	rm -f thermocouple
	rm -f *.o
