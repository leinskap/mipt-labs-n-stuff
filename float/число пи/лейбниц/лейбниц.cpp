#include <iostream>
using namespace std;
float pi(long long int n)
{
    float sum = 0.0;
    int sign = 1;
    for (long long int i = 0; i < n; ++i)
    {
        sum += sign/(2.0*i+1.0);
        sign *= -1;
    }
    return 4.0*sum;
}
int main()
{
    cout << fixed;
    cout.precision(7);
    for(long long int i=0;i<10000;i++)
    {
        cout<<pi(i)<<end;
    }
    return 0;
}
