#include "timer.h"

#include <ctime>
#include <chrono>
#include <iostream>

void Timer::start()
{
  this->startTime = std::chrono::steady_clock::now();
}

void Timer::stop()
{
  auto endTime = std::chrono::steady_clock::now();
  auto elapsedTime = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime);
  std::cout << elapsedTime.count() << " ms passed" << std::endl;
}
