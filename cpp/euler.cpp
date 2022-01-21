#include "euler.h"
#include <vector>
#include <cstdint>
#include <string>


std::vector<uint64_t> primeFactors(uint64_t n)
{
  std::vector<uint64_t> factors;
  if(isPrime(n))
    {
      factors.push_back(n);
      return factors;
    }
  

  while(n % 2 == 0)
    {
      factors.push_back(2);
      n /= 2;
    }

  for(int i = 3; i < sqrt(n) + 1; i += 2)
    {
      while(n % i == 0)
	{
	  factors.push_back(i);
	  n /= i;
	}
    }

  if(n > 2)
    {
      factors.push_back(n);
    }

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

bool isPalindrome(int n)
{
  auto s = std::to_string(n);
  auto original = s;

  reverse(s.begin(), s.end());

  return original == s;
}

int *bubbleSort(int *arr)
{
  return NULL;
}
