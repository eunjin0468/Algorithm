#include <stdio.h>
// (0 < A, B < 10)
int main(){
    int a=1; int b=1;
    
    while(scanf("%d %d", &a, &b)!=EOF){
        printf("%d\n", a+b);
    }
    return 0;
}