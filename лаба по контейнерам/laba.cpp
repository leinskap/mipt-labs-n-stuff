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
//    ofstream out;
//    out.open("data.txt");
//    // Задаём количество элементов
//    int n;
//    cin >> n;
//    vector<unsigned int> v;
//
//    // Заполняем вектор и измеряем время
//    for (int i = 0; i < n; i++)
//    {
//        v.push_back(i);
//        out << i << ' ' << v.size() << ' ' << v.capacity() << endl;
//    }
//    out.close();




    int n_max = 1000;
    int repeats = 1000;
    ofstream out;
//    out.open("data1-1.txt");
//    vector<unsigned int> v;
//    v.push_back(0);
//    //vector<double> time;
//    out << std::fixed << std::setprecision(10);
//    for (int n=65500; n<=65600;n++)
//    {
//        double time = 0;
//        for (int i=0;i<repeats;i++)
//        {
//            v.resize(0);
//
//            for (int j=0;j<n;j++)
//            {
//                v.push_back(j);
//            }
//            if (i==0) {cout<<n<<' '<<v.capacity()<<' ';}
//            double start = get_time();
////            v.insert(v.begin(), 1);
//            v.push_back(1);
//            double finish = get_time();
//            time += finish - start;
//            if (i==0) {cout<<v.capacity()<<endl;}
//
//        }
//
//            //time.push_back(total);
//
//        out << n << ' ' << time/repeats << endl;
//    }

    out.open("data2-2.txt");
    vector<unsigned int> v;
    v.push_back(0);
    //vector<double> time;
    out << std::fixed << std::setprecision(10);
    for (int n=1; n<=100000;n*=2)
    {
        cout<<n<<endl;
        double time = 0;
        for (int i=0;i<repeats;i++)
        {
            v.resize(0);

            for (int j=0;j<n;j++)
            {
                v.push_back(j);
            }
            //if (i==0) {cout<<n<<' '<<v.capacity()<<' ';}
            double start = get_time();
//          v.insert(v.begin(), 1);
            //v.push_back(1);
            v.erase(v.begin() + rand_uns(0, n-1));
            double finish = get_time();
            time += finish - start;
            //if (i==0) {cout<<v.capacity()<<endl;}

        }

            //time.push_back(total);

        out << n << ' ' << time/repeats << endl;
    }


    return 0;
}
