#include <stdio.h>

int main()
{
	unsigned int i = 1;

	char *c = (char*)&i;

	printf("Value of C = %d\n", *c);

	if(*c) 
	{
		printf("Little Endian");
	}

	else 
	{
		printf("Big Endian");
	}

	// int x = 4;
	// float *y = (float*)&x;

	// printf("Value of y = %f", *y);
}