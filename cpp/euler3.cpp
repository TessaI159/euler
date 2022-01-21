#include "timer.h"
#include "euler.h"
#include <iostream>


int main(int argc, char** args)
{
  Timer timer;
  timer.start();

  std::cout << primeFactors(600851475143).back() << std::endl;
  
  timer.stop();
  return 0;
}
