#include "timer.h"
#include "euler.h"
#include <iostream>

int main(int argc, char** args)
{
  Timer timer;
  timer.start();
  std::cout << squareOfSums(42) << std::endl;
  std::cout << sumOfSquares(42) << std::endl;
  timer.stop();
  return 0;
}


