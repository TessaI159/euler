// Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

// By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
#include "timer.h"
#include <iostream>


int main(int argc, char** args)
{
  Timer timer;
  timer.start();
  int answer{0};
  int current{0};
  int previous{1};

  
  while(current < 4000000)
    {

      int temp = current;
      
      current += previous;
      previous = temp;
      
      if(current % 2 == 0)
	{
	  answer += current;
	}
    }
  
  std::cout << answer << std::endl;
  timer.stop();
  return 0;
}
