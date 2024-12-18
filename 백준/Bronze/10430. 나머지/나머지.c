#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
    int a=0, b=0, c=0;
    int out1=0, out2=0, out3=0, out4=0;
    scanf("%d %d %d", &a, &b, &c);

    out1 = (a+b)%c;
    out2 = ((a%c)+(b%c))%c;
    out3 = (a*b)%c;
    out4 = ((a%c)*(b%c))%c;
    printf("%d\n", out1);
    printf("%d\n", out2);
    printf("%d\n", out3);
    printf("%d\n", out4);
}
