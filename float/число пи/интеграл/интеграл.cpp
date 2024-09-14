#include <iostream>
#include <math.h>
using namespace std;
float f(float x)
{
    return sqrt(1-pow(x,2));
}
int main()
{
    cout<<fixed;
    cout.precision(7);
    float integration;
    integration = f(0) + f(1);
    for (long long int n=1; n<=10000; n++)
    {
        for (int i=1; i<n; i++)
        {
            integration += 2*f(static_cast<float>(i)/n);
        }
        integration = integration/(2*n);
        cout<<integration*4<<endl;
    }
    return 0;
}
