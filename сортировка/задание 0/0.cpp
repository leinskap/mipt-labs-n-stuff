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
double BubbleSort(long long int n)
{
    int arr[100000]={0};
    for (long long int i=0;i<n;i++)
    {
        arr[i]=rand_uns(0,100000);
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

//Сортировка выбором
double SelectionSort(long long int n)
{
    int arr[100000]={0};
    for (long long int i=0;i<n;i++)
    {
        arr[i]=rand_uns(0,100000);
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

//Сортировка вставкой
double InsertSort(long long int n)
{
    int arr[100000]={0};
    for (long long int i=0;i<n;i++)
    {
        arr[i]=rand_uns(0,100000);
    }
    auto start = chrono::steady_clock::now();
    for (long long int i=1;i<n;i++)
    {
        for (long long int j=i;j>0;j--)
        {
            if (arr[j-1]>arr[j])
            {
                swap(arr[j-1],arr[j]);
            }
        }

    }
    auto end = chrono::steady_clock::now();
    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    return time;
}

//Функции для расчёта среднего времени выполнения сортировки
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
void InsertSortMeanTime(long long int n)
{
    double meanTime = 0;
    cout<<"Insert Sort"<<endl;
    for (long long int i = 1;i <= n;i *= 2)
    {
        for (int j=0;j<100;j++)
        {
            meanTime += InsertSort(i);
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
    BubbleSortMeanTime(10000);
    SelectionSortMeanTime(10000);
    InsertSortMeanTime(10000);



}
