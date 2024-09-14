#include <iostream>
#include <chrono>
#include <math.h>
using namespace std;
using namespace std;
float piCalc(long long int n)
{
    float pi, ans, ans1, a = 0;
    for (long long int i=1;i<n;i++)
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
    cout.precision(10);
    auto start = std::chrono::steady_clock::now();
    for(long long int i=0;i<1000000;i++)
    {
        float pi = piCalc(i);
        cout<<pi<<endl;
        if (pi>=3.1415 && pi<3.1416)
        {
            break;
        }
    }
    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    printf("The time: %f microseconds\n", time);
}
