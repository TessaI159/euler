#include "timer.h"
#include "euler.h"
#include <iostream>

int main(int argc, char** args)
{
  Timer timer;
  timer.start();
  int sortMe[] = {41, 15, 17, 32, 18, 28, 77, 54};
  timer.stop();
  return 0;
}


