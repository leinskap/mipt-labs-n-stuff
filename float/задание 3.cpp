#include <iostream>
using namespace std;
int main()
{
    cout << fixed;
    cout.precision(2);
    for(float i=1;i<16777217;i+=1)
    {
        cout<<i<<endl;
    }
    return 0;
}
