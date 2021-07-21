#include <stdio.h>  
int main(int argc, char *argv[]) 
{ 
    int i =  0 ; 

    printf( "execute my command!\n" ); 
    for (i =  0  ;i < argc;i++) 
    { 
       printf( "input param:%d - %s\n" ,i,argv[i]);  
    } 
    return  1 ; 
}