// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include <stdio.h>

int main(int argc, char * * argv)
{
  int i, j;
  for(i = 20; ; ++i) {
    int flag = 1;
    for(j = 1; j <= 20; ++j) {
      if(i % j != 0) {
	flag = 0;
	break;
      }
    }
    if(flag == 1) {
      printf("Our smallest, evenly divisible number is: %d\n", i);
      break;
    }
  }
  return 0;
}
