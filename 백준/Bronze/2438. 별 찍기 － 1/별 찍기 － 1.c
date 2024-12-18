#include <stdio.h>
int main(){
    int n=0;
    int k=0;
    scanf("%d", &n);
    
    
    for(int i=0; i<n; i++){
        for(k=0; k<i+1; k++){
            printf("*");
        }
        printf("\n");
    }
}