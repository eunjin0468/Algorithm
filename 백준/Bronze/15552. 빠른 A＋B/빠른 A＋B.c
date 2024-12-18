#include <stdio.h>

int main(){
    int t;
    scanf("%d", &t);
    /*if(t>0 && t<1000000){
        printf("%d\n", t);
    }*/
    
    for(int i=0; i<t; i++){
        int a=0;
        int b=0;
        //if(a>1 && b>1){
          //  if(1000>a && 1000>b){
                scanf("%d %d", &a,&b); 
            //}
      //  }
        printf("%d\n", a+b);
        
    }
    
}