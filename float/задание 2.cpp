#include <iostream>
using namespace std;
unsigned int power(unsigned int n,unsigned int base)
{
    if (base==0)
        return 1;
    int k=n;
    for (int i=0;i<base-1;i++)
        n*=k;
    return n;
}
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
    cout << fixed;
    cout.precision(2);
    for (int i = 0; i<50; i++)
    {
        cout<<power(10,i)<<endl;
        intToBinary(power(10,i));
        cout<<'\n';
    }
    return 0;
}
