#include <chrono>
#include <random>
#include <iostream>
using namespace std;
int rand_uns(int min, int max)
{
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}

double quickSort(int *arr, int left, int right)
{
    auto start = chrono::steady_clock::now();
    if (left<right)
    {
        int i=left;
        int j=right;
        int x = arr[(left + right) / 2];
        while(i<=j)
        {
            while(arr[i] < x)
            {
                i+=1;
            }
            while(arr[j] > x)
            {
                j-=1;
            }
            if (i<=j)
            {
                swap(arr[i],arr[j]);
                i+=1;
                j-=1;
            }
        }
        quickSort(arr,left,j);
        quickSort(arr,i,right);
    }
    auto end = chrono::steady_clock::now();
    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    return time;
}
void meanTime()
{

}

int main()
{
    int arr[100000]={0};
    long long int n = 100000;

    cout<<fixed;
    cout.precision(1);
    for (long long int i = 0; i<=n; i+=10000)
    {
        for (long long int j=0;j<n;j++)
        {
            arr[j]=n-j;
        }
        double meanTime = 0;
        for (int k=0;k<100;k++)
        {
            meanTime+=quickSort(arr,0,i-1);
        }
        cout<<meanTime/100<<','<<' ';


    }
}
