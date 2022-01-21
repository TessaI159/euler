#ifndef TIMER_H
#define TIMER_H

#include <ctime>

class Timer
{
 public:
  void start();
  void stop();
  

 private:
  clock_t startTime;
  double elapsedTime;
};

#endif
