#include <iostream>
#include <chrono>
using namespace std;
float pi(long long int n) {
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
    cout<<fixed;
    cout.precision(10);
    auto start = chrono::steady_clock::now();
    for(long long int i=0;i<100000000;i++)
    {

        float p=pi(i);
        if (p>=3.14 && p<3.15)
        {
            break;
        }
    }
    auto end = chrono::steady_clock::now();
    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    cout<<time;
}
