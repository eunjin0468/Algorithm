/*Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7*/

#include <stdio.h>
//a>0, b<10
int main(){
    int n=0;
    scanf("%d", &n);
    
    for(int i=0; i<n; i++){
        int a=0; int b=0;
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d + %d = %d\n", i+1, a,b, a+b);
    }
}