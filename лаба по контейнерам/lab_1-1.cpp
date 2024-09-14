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
    int repeats = 1000;
    ofstream out;
    out.open("data1-1.txt");
    vector<unsigned int> v;
    v.push_back(0);
    out << std::fixed << std::setprecision(10);
    for (int n=1000; n<=4100;n++)
    {
        double time = 0;
        for (int i=0;i<repeats;i++)
        {
            v.resize(0);
            for (int j=0;j<n;j++) {v.push_back(j);}
            if (i==0) {cout<<n<<' '<<v.capacity()<<' ';}
            double start = get_time();
            v.insert(v.begin()+rand_uns(0, n-1), 1);
            double finish = get_time();
            time += finish - start;
            if (i==0) {cout<<v.capacity()<<endl;}
        }
        out << n << ' ' << time/repeats << endl;
    }
    return 0;
}

