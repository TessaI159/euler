#!/bin/zsh

g++ -std=c++17 -Itimer.h timer.cpp euler.cpp euler$1.cpp -o euler$1.run
