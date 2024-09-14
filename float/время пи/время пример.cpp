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
    auto start = std::chrono::steady_clock::now();
    for(long long int i=0;i<100000000;i++)
    {

        float p=pi(i);
        if (p>=3.1415926 && p<3.1415927)
        {
            break;
        }
    }
    auto end = std::chrono::steady_clock::now();
    auto elapsed = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    printf("The time: %f microseconds\n", time);
}
