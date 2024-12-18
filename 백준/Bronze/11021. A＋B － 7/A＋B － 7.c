#include <stdio.h>
/*  5
    1 1
    2 3
    3 4
    9 8
    5 2*/
/*Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7*/

int main(){
    //반복할 숫자 입력받기
    int n;
    scanf("%d", &n);
    
    for(int i=0; i<n; i++){
        //두개의 정수값 입력받기
        int a=0;
        int b=0;
        scanf("%d %d", &a, &b);
        if(a>0 && b<10){
           printf("Case #%d: %d\n", i+1, a+b); 
        }
        
    }
}