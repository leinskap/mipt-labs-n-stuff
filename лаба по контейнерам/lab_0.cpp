#include <iostream>
#include <vector>
#include <fstream>
using namespace std;
int main()
{
    ofstream out;
    out.open("data.txt");
    int n = 1000;
    vector<unsigned int> v;
    for (int i = 0; i < n; i++)
    {
        v.push_back(i);
        out << i << ' ' << v.size() << ' ' << v.capacity() << endl;
    }
    out.close();
    return 0;
}

