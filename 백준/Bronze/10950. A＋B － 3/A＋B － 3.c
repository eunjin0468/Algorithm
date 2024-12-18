#include <stdio.h>

int main(){
    //반복할 숫자 입력받기
    int n;
    scanf("%d", &n);
    
    for(int i=0; i<n; i++){
        int a=0, b=0;
        scanf("%d %d", &a, &b);
        if(a>0 && b<10){
           printf("%d\n", a+b); 
        }
    }
    
        
    
}