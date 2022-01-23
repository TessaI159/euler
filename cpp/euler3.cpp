// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?

#include "timer.h"
#include "euler.h"
#include <iostream>


int main(int argc, char** args)
{
  Timer timer;
  timer.start();
  int answer = primeFactors(600851475143).back();
  std::cout << answer << std::endl;
  
  
  timer.stop();
  return 0;
}
