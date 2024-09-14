
#include <iostream>
#include <random>
#include <chrono>
#include<cmath>
#include<vector>
#include <iomanip>
#include <fstream>
template <typename dataType>
class subvector
{
public:
    subvector();
    ~subvector();
    bool Push_back(dataType d);
    int pop_back();
    bool resize(unsigned int new_capacity);
    void shrink_to_fit();
    void clear();
    int getMas(int i);
    unsigned int getCapacity();
    unsigned int getTop();
    bool insert(unsigned int place, dataType elem);
    bool erase(unsigned int place);
private:
    dataType* mas;
    unsigned int top;
    unsigned int capacity;
};
template <typename dataType>
unsigned int subvector<dataType>::getTop()
{
    return this->top;
}
template <typename dataType>
unsigned int subvector<dataType>::getCapacity()
{
    return this->capacity;
}
template <typename dataType>
int subvector<dataType>::getMas(int i)
{
    return this->mas[i];
}
template <typename dataType>
subvector<dataType>::subvector()
{
    this->mas = nullptr;
    this->top = 0;
    this->capacity = 0;
}
template <typename dataType>
subvector<dataType>::~subvector()
{
    if (this->capacity>0)
        delete[] this->mas;
    this->top = 0;
    this->capacity = 0;
}
template <typename dataType>
bool subvector<dataType>::Push_back(dataType d)
{
    if (this->capacity == this->top)
    {
        bool del = false;
        if(this->capacity==0)
            this->capacity += 1;
        else
        {
            this->capacity*=2;
            del = true;
        }
        int *new_mas = new dataType[this->capacity];
        for (unsigned int i=0;i<this->top;i++)
        {
            new_mas[i] = this->mas[i];
        }
        if(del)
            delete[] this->mas;
        this->mas = new_mas;
    }
    this->top+=1;
    this->mas[this->top-1]=d;
    return true;
}
template <typename dataType>
int subvector<dataType>::pop_back()
{
    if (this->top == 0)
    {
        return 0;
    }
    this->top-=1;
    return this->mas[this->top];
}
template <typename dataType>
bool subvector<dataType>::resize(unsigned int new_capacity)
{
    if (new_capacity==0)
    {
        if (this->capacity>0)
        {
            delete[] this->mas;
            this->top=0;
            this->capacity=0;
        }
        return true;
    }
    int *new_mas = new dataType[new_capacity];
    for (unsigned int i=0;i<std::min(this->top, new_capacity);i++)
    {
        new_mas[i] = this->mas[i];
    }
    if (this->capacity>0)
        delete[] this->mas;
    this->capacity = new_capacity;
    this->mas = new_mas;
    return true;
}
template <typename dataType>
void subvector<dataType>::shrink_to_fit()
{
    resize(this->top);
}
template <typename dataType>
void subvector<dataType>::clear()
{
    this->top = 0;
}
template <typename dataType>
bool subvector<dataType>::insert(unsigned int place, dataType elem)
{
    if (this->top+1>this->capacity)
    {
        resize(this->capacity*2);
    }
    int *new_mas = new dataType[this->capacity];
    for (unsigned int i=0;i<std::min(this->top, this->capacity);i++)
    {
        if (i==place)
        {
            new_mas[i] = elem;
            i+=1;
        }
        new_mas[i] = this->mas[i];
    }
    if (this->capacity>0)
        delete[] this->mas;
    this->mas = new_mas;
    return true;

}
template <typename dataType>
bool subvector<dataType>::erase(unsigned int place)
{
    int *new_mas = new dataType[this->capacity-1];
    for (unsigned int i=0;i<std::min(this->top, this->capacity);i++)
    {
        if (i==place)
        {
            i+=1;
        }
        new_mas[i] = this->mas[i];
    }
    if (this->capacity>0)
        delete[] this->mas;
    this->mas = new_mas;
    return true;

}

using std::cout;
using std::endl;
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

