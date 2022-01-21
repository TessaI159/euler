#include "euler.h"
#include <vector>


std::vector<int> primeFactors(int n)
{
  std::vector<int> factors;
  return factors;
}


bool isPrime(int n)
{
  if(n < 2)
    {
      return false;
    }
  else if(n == 2)
    {
      return true;
    }
  else if(n % 2 == 0)
    {
      return false;
    }
  else
    {
      for(int i = 2; i < sqrt(n) + 1; ++i)
	{
	  if(n % i == 0)
	    {
	      return false;
	    }
	}
    }
  return true;
      
}
