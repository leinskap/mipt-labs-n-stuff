#include <iostream>
#include <chrono>
#include <random>
using namespace std;

//Функция для вывода случайных числел
int rand_uns(int min, int max)
{
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}

//Сортировка пузырьком
double BubbleSort(int *arr,long long int n)
{
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
int main()
{
    int arr[8192]{0};
    long long int n=8192;
    for(long long i =0;i<n;i+=1)
    {
        arr[i]=n-i;
    }
    cout<<fixed;
    cout.precision(1);
    for (long long i=0;i<100;i++)
    {
        cout<<BubbleSort(arr,n)<<','<<' ';
    }
    return 0;
}
