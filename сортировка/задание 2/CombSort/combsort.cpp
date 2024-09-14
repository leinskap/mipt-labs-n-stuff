#include<bits/stdc++.h>
#include <chrono>
#include <iostream>
#include <random>
using namespace std;
int rand_uns(int min, int max)
{
    unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}
using namespace std;
int getNextGap(int gap)
{
	gap = (gap*10)/13;

	if (gap < 1)
		return 1;
	return gap;
}
double combSort(int *a, int n)
{
	int gap = n;
	bool swapped = true;
	auto start = chrono::steady_clock::now();
	while (gap != 1 || swapped == true)
	{
		gap = getNextGap(gap);
		swapped = false;
		for (int i=0; i<n-gap; i++)
		{
			if (a[i] > a[i+gap])
			{
				swap(a[i], a[i+gap]);
				swapped = true;
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
    int arr[100000]{0};
    for (int n=0;n<=100000;n+=10000)
    {
        for (int i = 0; i<n;i++)
        {
            arr[i] = rand_uns(0,n);
        }
        double meanTime = 0;
        for (int j=0;j<100;j++)
        {
            meanTime += combSort(arr,n);

        }
        cout<<meanTime/100.0<<','<<' ';

    }
}
