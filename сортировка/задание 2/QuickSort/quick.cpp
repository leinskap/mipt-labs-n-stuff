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

