#include "timer.h"

#include <ctime>
#include <iostream>

void Timer::start()
{
  this->startTime = clock();
}

void Timer::stop()
{
  this->elapsedTime = (clock() - startTime);
  std::cout << this->elapsedTime << " ms passed" << std::endl;
}
