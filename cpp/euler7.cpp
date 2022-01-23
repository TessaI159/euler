// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

// What is the 10 001st prime number?

#include "timer.h"
#include "euler.h"
#include <iostream>

int main(int argc, char** args)
{
  Timer timer;
  timer.start();
  int index = 1;
  for(int i = 3; ; ++i)
    {
      if(isPrime(i))
	{
	  index++;
	}
      if(index == 10001)
	{
	  std::cout << i << std::endl;
	  break;
	}
    }
  timer.stop();
  return 0;
}


