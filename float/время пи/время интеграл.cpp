#include <iostream>
#include <chrono>
#include <math.h>
using namespace std;


float f(float x)
{
    return sqrt(1-pow(x,2));
}


int main()
{
    cout<<fixed;
    cout.precision(10);
    auto start = std::chrono::steady_clock::now();
    float integration;
    integration = f(0) + f(1);
    for (long long int n=1; n<=10000000; n++)
    {
        for (int i=1; i<n; i++)
        {
            integration += 2*f(static_cast<float>(i)/n);
        }
        integration = integration/(2*n);
        float pi = integration*4;
        if (pi>=3.1415926 && pi<3.1415927)
            break;
    }


    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    printf("The time: %f microseconds\n", time);
}

