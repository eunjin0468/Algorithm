#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
    int h, m;
    scanf("%d %d", &h, &m);
    if (m >= 45 && h>0) {
        printf("%d %d", h, m - 45);
    }
    else if (m < 45 && h>0) {
        printf("%d %d", h - 1, m + 15);
    }
    else if (m < 45 && h == 0) {
        printf("23 %d", m + 15);
    }
    else if (h == 0 && m >= 45) {
        printf("0 %d", m - 45);
    }
}
