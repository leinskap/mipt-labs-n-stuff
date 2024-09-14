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
