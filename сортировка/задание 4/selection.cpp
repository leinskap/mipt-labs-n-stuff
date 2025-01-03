#include <iostream>
#include <chrono>
#include <random>
using namespace std;

//������� ��� ������ ��������� ������
int rand_uns(int min, int max)
{
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}


double SelectionSort(long long int n)
{
    int arr[100000]={0};
    for (long long int i=0;i<n;i+=1)
    {
        arr[i]=n-i;
    }
    long long int m = 0;
    auto start = chrono::steady_clock::now();
    for (long long int i=0;i<n-1;i++)
    {
        for (long long int j=i+1;j<n;j++)
        {
            if (arr[i]<arr[m])
            {
                m=j;
            }
        }
        if (i != m)
        {
            swap(arr[i],arr[m]);
        }
    }
    auto end = chrono::steady_clock::now();
    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    return time;
}




void SelectionSortMeanTime(long long int n)
{
    double meanTime = 0;
    cout<<"Selection Sort"<<endl;
    for (long long int i = 1;i <= n;i *= 2)
    {
        for (int j=0;j<100;j++)
        {
            meanTime += SelectionSort(i);
        }
        cout<<(meanTime/100.0)<<','<<' ';
    }
    cout<<'\n';
}

int main()
{
    cout<<fixed;
    cout.precision(1);
    for (long long int i = 1;i <= 10000;i *= 2)
    {
        cout<<i<<','<<' ';
    }
    cout<<'\n';
    SelectionSortMeanTime(10000);



}
