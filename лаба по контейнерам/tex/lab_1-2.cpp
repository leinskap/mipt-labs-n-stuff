int main()
{
    std::cout << std::fixed;
    std::cout.precision(10);
    std::ofstream out;
    out.open("data1-2.txt");
    out << std::fixed << std::setprecision(10);
    std::vector<double> time;
    double start = 0, finish = 0, total = 0;
    typedef subvector<int> mysv;
    mysv v;
    int repeats = 1000;
    for (int n=4000; n<=4200;n++)
    {
        double time = 0;
        for (int i=0;i<repeats;i++)
        {
            v.resize(0);

            for (int j=0;j<n;j++) {v.Push_back(j);}
            double start = get_time();
            v.insert(rand_uns(0, n-1), 1);
            double finish = get_time();
            time += finish - start;
        }
        out << n << ' ' << time/repeats << endl;
    }
    return 0;
}

