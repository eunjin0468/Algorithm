#include <stdio.h>

int main(){
    int x,y;
    scanf("%d",&x);
    scanf("%d",&y);
   
    if(x==0){
        printf("ㄷㅏㅅㅣ ㅇㅣㅂㄹㅕㄱ");
        scanf("%d",&x);
    }
    if(y==0){
        printf("ㄷㅏㅅㅣ ㅇㅣㅂㄹㅕㄱ");
        scanf("%d",&y);
    }
    if(0<=x&&x<=1000&&0<=y&&y<=1000){
        printf("1");
    }
    if(0<=x&&x<=1000&&-1000<=y&&y<=0){
        printf("4");
    }
   if(-1000<=x&&x<=0&&-1000<=y&&y<=0){
        printf("3");
    }
    if(-1000<=x&&x<=0&&0<=y&&y<=1000){
        printf("2");
    }

}