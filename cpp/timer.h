#ifndef TIMER_H
#define TIMER_H

#include <ctime>
#include <chrono>

class Timer
{
public:
  void start();
  void stop();

private:
  std::chrono::steady_clock::time_point startTime;
  std::chrono::steady_clock::time_point endTime;

};

#endif
