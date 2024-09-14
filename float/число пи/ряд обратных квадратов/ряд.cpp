#include <iostream>
#include <math.h>
using namespace std;
float piCalc(float n)
{
    float pi, ans, ans1, a = 0;
    for (float i=1;i<n;i++)
    {
        a=i*i;
        ans+=1/a;
    }
    ans1=6*ans;
    pi=sqrt(ans1);
    return pi;
}
int main()
{
    cout<<fixed;
    cout.precision(7);
    for(float i=0.0;i<10000.0;i++)
    {
        cout<<piCalc(i)<<endl;
    }
    return 0;
}
