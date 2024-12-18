#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
    int a[9] = { 0, };
    int max = 0;
    int i = 0,b=0;

    for ( i = 0; i < 9; i++) {
        scanf("%d", &a[i]);
        if (a[i] > max) {
            max = a[i];
            b = i;
        }
    }
    printf("%d\n%d", max,b+1);
}