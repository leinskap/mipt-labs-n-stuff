
void heapify(int *arr, int n, int root)
{
    int largest = root;
    int left = 2*root + 1;
    int right = 2*root + 2;
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != root)
    {
        swap(arr[root], arr[largest]);

        heapify(arr, n, largest);
    }
}
double heapSort(int *arr, int n)
{
    auto start = chrono::steady_clock::now();
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i=n-1; i>=0; i--)
    {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
    auto end = chrono::steady_clock::now();
    auto elapsed = chrono::duration_cast<chrono::microseconds>(end - start);
    double time = (double)(elapsed.count());
    return time;
}
