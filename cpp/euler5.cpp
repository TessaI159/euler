// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include "timer.h"
#include "euler.h"
#include <iostream>


int main(int argc, char** args)
{
  Timer timer;
  timer.start();

  const int constraint = 20;
  int current = constraint;
  bool looping = true;
  int div = 2;
  
  while(looping)
    {
      if(current % div != 0)
	{
	  div = 2;
	  current += constraint;
	}
      else if(current % div == 0 & div == constraint)
	{
	  looping = false;
	}
      div += 1;
    }
  std::cout << current << std::endl;
  timer.stop();
  return 0;
}
