#include <iostream>
using namespace std;
union floatNumber
{
    float floatPart;
    unsigned int intPart;
};
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
}
int main()
{
    floatNumber a;
    cin>>a.floatPart;
    intToBinary(a.intPart);
    return 0;
}
