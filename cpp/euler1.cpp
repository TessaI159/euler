// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.

#include "timer.h"
#include <iostream>

int naiveMethod(int n);
int sumArithSeq(int b, int e);
int mathMethod(int n);


int main(int argc, char** args)
{
  Timer timer;
  timer.start();
  int answer = mathMethod(1000);
  std::cout << answer << std::endl;
  timer.stop();
  return 0;
}

int naiveMethod(int n)
{
  int total{0};
  for(int i{0}; i < n; ++i)
    {
      if(i % 3 == 0 | i % 5 == 0)
	total += i;
    }
  return total;
}

int sumArithSeq(int b, int e)
{
  // This uses the equation (n * (n + 1)) / 2 then multiplies it by b
  // This adds up to every number divisible by b from [1,e)
  
  return ((((e - 1) / b) * (((e - 1) / b) + 1)) >> 1) * b;
}

int mathMethod(int n)
{
  // We subtract the numbers divisible by fifteen because we add them
  // in twice. Once when we add the 3s, once when we add the 5s
  return sumArithSeq(3,n) + sumArithSeq(5,n) - sumArithSeq(15,n);
}
