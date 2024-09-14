#include <iostream>
using namespace std;
void  intToBinary(unsigned int num)
{
    int i=0;
    for(int i=0;i<32;i++)
    {
        if (num == (num<<1)>>1)
            cout<<0;
        else
            cout<<1;
        num = num<<1;
    }
    cout<<'\n';
}
int main()
{
    int n;
    cin>>n;
    intToBinary(n);
    return 0;
}
