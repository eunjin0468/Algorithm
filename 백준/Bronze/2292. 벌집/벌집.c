#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define size 1001
int cnt[size] = { 0, };

int main() {
	int n,i=2, j=5, cnt=2;
	scanf("%d", &n);

	if (n == 1) {
		printf("1");
		return 0;
	}
	else {
		while (1) {
			if(n>=i && i+j >=n){
				printf("%d", cnt);
				break;
		}
			i = i + j + 1;
			j += 6;
			cnt++;
        }
    }
}