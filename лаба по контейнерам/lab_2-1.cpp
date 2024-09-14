#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <cstdlib>
#include <chrono>
#include <random>
#include <chrono>
#include <cmath>
#include <vector>
#include <iomanip>
#include <fstream>
using namespace std;
double get_time()
{
    return std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::steady_clock::now().time_since_epoch()).count()/1e6;
}
int rand_uns(int min, int max)
{
        unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
        static std::default_random_engine e(seed);
        std::uniform_int_distribution<int> d(min, max);
        return d(e);
}
int main()
{
    int n_max = 1000;
    int repeats = 1000;
    ofstream out;
    out.open("data2-1.txt");
    vector<unsigned int> v;
    v.push_back(0);
    out << std::fixed << std::setprecision(10);
    for (int n=1; n<=100000;n*=2)
    {
        double time = 0;
        for (int i=0;i<repeats;i++)
        {
            v.resize(0);
            for (int j=0;j<n;j++) {v.push_back(j);}
            double start = get_time();
            v.erase(v.begin() + rand_uns(0, n-1));
            double finish = get_time();
            time += finish - start;
        }
        out << n << ' ' << time/repeats << endl;
    }
    return 0;
}

