#include <iostream>
#include <chrono>
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
    cout.precision(10);
    auto start = std::chrono::steady_clock::now();
    for(long unsigned int i=0;i<10000000;i++)
    {
        float pi = 4.0*(4.0*xCalc(0.2,i)-xCalc(0.00418410041841004184,i));
        if (pi>=3.1415926 && pi<3.1415927)
        {
            break;
        }
    }
    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    printf("The time: %f microseconds\n", time);
    return 0;
}
