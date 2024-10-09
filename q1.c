#include<stdio.h>
void main()
{
    int n,i,sum=0,a=5;
    printf("Enter 5 numbers\n");

    for(i=1;i<=a;i++)
    {
        scanf("%d",&n);
        int l=n%10;
        sum=sum+l;
    }
        printf("Sum of last digits = %d",sum);
}  