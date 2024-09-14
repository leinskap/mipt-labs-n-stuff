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
