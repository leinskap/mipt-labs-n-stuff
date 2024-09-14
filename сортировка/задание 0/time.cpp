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
