// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

// Find the largest palindrome made from the product of two 3-digit numbers.

#include "timer.h"
#include "euler.h"
#include <iostream>
#include <ctime>


int main(int argc, char** args)
{
  Timer timer;
  timer.start();

  int *productsOfThree = new int [810000];
  int index = 0;
  for(int i = 100; i < 1000; ++i)
    {
      for(int j = i; j < 1000; ++j)
	{
	  if(isPalindrome(i * j))
	    {
	      productsOfThree[index++] = i * j;
	    }
	}
    }

  int largest = 0;
  for(int i = 0; i < 810000; ++i)
    {
      if(productsOfThree[i] > largest)
	{
	  largest = productsOfThree[i];
	}
      if(productsOfThree[i] == 0)
	{
	  std::cout << largest << std::endl;
	  timer.stop();
	  break;
	}
    }
  
  return 0;
}

