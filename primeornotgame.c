// GUESS A PRIME NUMBER ^^ 
#include <stdio.h> 
void prime (int) ;
int main () {
    int run = 1 , stop ; 
    while (run) {
        printf("Guess a prime number :3\n") ; 
        printf("Press 1 to play or 0 to quit:\n") ;
        scanf("%d" , &stop) ; 
        if (stop == 0) {
            printf("Bye bye ^^") ;
            run = 0 ; 
        } else if (stop == 1) {
            int a ; 
            printf("Enter a natural number below:\n") ; 
            scanf("%d" , &a) ; 
            prime (a) ; 
        } else {
            printf("Enter a valid number you idiot -_-\n\n") ;
        }
    }
    return 0 ; 
}
void prime (int a) {
    int check = 1 ;
    if (a == 1) {
        printf("1 is niether prime nor composite. :p\n") ; 
    } else if (a == 2) {
        printf("Given number is prime.\n") ;
        printf("Congratulations on finding a prime number : ) \n") ;  
    } else if (a > 2) {
        for (int i = 2 ; i < a ; i++) {
            if (a % i == 0) {
                check = 0 ;
                printf("%d is a factor.\n" , i) ;
            }
        }
        if (check == 1) {
            printf("Given number is prime.\n") ;
            printf("Congratulations on finding a prime number : )\n") ; 
            if (a < 101 && a > 0) {
                printf("Now try a bigger number if you got balls :/ Be careful of integer limit though -_- \n\n") ; 
            } else {
                printf("Try with a bigger number :D just try not to exceed integer limit.\n\n") ;
            } 
        } else {
            printf("Given number is composite.\n") ; 
            printf("Better luck next time :O\n\n") ; 
        }
    } else {
        printf("Enter a valid number -_-\n") ; 
    } 
}
            

     
