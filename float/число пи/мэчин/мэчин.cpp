#include <iostream>
#include <math.h>
using namespace std;
float xCalc(float x, long unsigned int n)
{
    float result =0.0;
    int sign = 1;
    long unsigned int k=1;
    for (long unsigned int i = 1; i<=n;i++)
    {
        result+=sign*pow(x,k)/k;
        k+=2;
        sign*=(-1);
    }
    return result;
}
int main()
{
    cout<<fixed;
    cout.precision(7);
    for(long unsigned int i=0;i<10000;i++)
    {
        cout<<4.0*(4.0*xCalc(0.2,i)-xCalc(0.0041841,i))<<endl;
    }
    return 0;
}
