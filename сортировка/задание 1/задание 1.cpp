#include <iostream>
#include <chrono>
#include <random>
using namespace std;
int rand_uns(int min, int max)
{
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}
double BubbleSort(long long int n)
{
    volatile int arr[10000]{0};
    for (long long int i=0;i<n;i++)
    {
        arr[i]=rand_uns(0,10000);
    }
    auto start = chrono::steady_clock::now();
    for (long long int i=0;i<n;i++)
    {
        for (long long int j=0;j<n-1;j++)
        {
            if (arr[i]<arr[j])
            {
                swap(arr[i],arr[j]);
            }
        }
    }
    auto end = chrono::steady_clock::now();
    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    return time;

}
void BubbleSortMeanTime(long long int n)
{
    double meanTime = 0;
    cout<<"Bubble Sort"<<endl;
    for (long long int i = 1;i <= n;i *= 2)
    {
        for (int j=0;j<100;j++)
        {
            meanTime += BubbleSort(i);
        }
        cout<<(meanTime/100.0)<<','<<' ';
    }
    cout<<'\n';

}
int main()
{
    cout<<fixed;
    cout.precision(1);
    BubbleSortMeanTime(10000);
}
