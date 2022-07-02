#include<stdlib.h>
#include<stdio.h>
#include<time.h>
/**
 * main -Entry point
 * Return: Always 0 (succcess)
 */
int main(void)
{
	int n;
	int last;
	/*your code goes there*/
	n = rand() - RAND_MAX / 2;
	last = n % 10;
	if (last > 5)
		printf("last of %i of %i and is greater than 5/n", last);
	else if (last == 0)
		printf("last of %i of %i and is 0/n", last);
	else if (last < 6)
		printf("last of %i of %i and is less than 6 and not 0/n", last);
         return (0);
}

