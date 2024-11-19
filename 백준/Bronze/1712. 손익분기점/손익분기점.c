#define  _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int a=0, b=0, c = 0;
	int i;
	scanf("%d %d %d", &a, &b, &c);
	
	if (b >= c) {
		printf("-1\n");
	}
	else
	{
		printf("%d\n", a / (c - b) + 1);
	}
}