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
