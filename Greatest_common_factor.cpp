#include <iostream>
#include<vector>
using namespace std;

// Brute-force method for GCD
int gcd(int a, int b) {
    int res = min(a, b);
    while (res > 0) {
        if (a % res == 0 && b % res == 0) {
            break;
        }
        res--;
    }
    return res;
}

// Euclidean method for GCD
int GCD(int a, int b) {
    while (a != b) {
        if (a > b) {
            a = a - b;
        } else {
            b = b - a;
        }
    }
    return a;
}

// Method for LCM
int lcm(int a, int b) {
    int res = max(a, b);
    while (true) {
        if (res % a == 0 && res % b == 0) {
            return res;
        }
        res++;
    }
}

// Method to check if a number is prime
bool isprime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

// Method to print the prime factors of a number
void primeFactors(int n) {
    for (int i = 2; i <= n; i++) {
        if (isprime(i)) {
            while (n % i == 0) {
                cout << i << " ";
                n /= i;
            }
        }
    }
    cout << endl;
}
void divisors(int n){
    for(int i=1;i<=n;i++){
        if(n%i==0){
            cout<<i<<endl;
        }
    }
}
// efficient solution
void divisors2(int n){
    int i;
    for(i=1;i*i<n;i++){
        if(n%i==0){
            cout<<i<<endl;
        }
    }    
    for(;i>=1;i--){
        if(n%i==0){
            cout<<n/i<<endl;
        }
    }    
    
}
void printprime(int n){
    for(int i;i<=n;i++){
        if(isprime(i)){
            cout<<i<<endl;
        }
    }
}
void sieve(int n){
    vector<bool> isprime(n+1,true);
    for(int i=2; i<=n;i++){
        if(isprime[i]){
            cout<<i<<endl;
            for(int j=i*i;j<=n; j=j+i){
                isprime[j]=false;
            }
        }
    }
}
int power(int x,int n){
    int res=1;
    for(int i=0;i<n;i++){
        res=res*x;
    }
    return res;
}
int iterative_power(int n, int x){
    int res=1;
    while(n>0){
        if(n%2!=0){
            res=res*x;
        }    
        x=x*x;
        n=n/2;
    }
    return res;
}
int main() {
    int result = gcd(50, 20);
    cout << "The greatest common divisor of 50 and 20 is: " << result << endl;

    int Result = GCD(100, 200);
    cout << "The greatest common divisor of 100 and 200 is: " << Result << endl;

    int res = lcm(4, 6);
    cout << "The LCM of 4 and 6 is: " << res << endl;

    bool ans = isprime(4);
    cout << "4 is prime: " << ans << endl;

    cout << "Prime factors of 50 are: ";
    primeFactors(50);
    divisors(60);
    divisors2(50);
    printprime(23);
    sieve(60);
    int select=power(2,3);
    cout<<"the result is:"<<select<<endl;
    int select2=iterative_power(3,2);
    cout<<"the result is:"<<select2<<endl;
    
    
    return 0;
}
