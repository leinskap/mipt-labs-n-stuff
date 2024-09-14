
#include <iostream>

struct subforwardlist
{
    int data;
    subforwardlist* next;
};

bool init(subforwardlist **sfl)
{
    (*sfl) = NULL;
    return true;
}

bool push_back(subforwardlist **sfl, int d)
{
    subforwardlist *tmp = new subforwardlist;
    tmp->data = d;
    tmp->next = NULL;
    if (*sfl==NULL)
    {
        *sfl = tmp;
        return true;
    }
    subforwardlist *tmp_sfl = (*sfl);
    while((tmp_sfl)->next != NULL )
    {
        (tmp_sfl) = (tmp_sfl)->next;
    }
    (tmp_sfl)->next = tmp;
    return true;
}

int pop_back(subforwardlist **sfl)
{
    int r;
    subforwardlist *pre_last = (*sfl);
    if ((*sfl)==NULL)
    {
        return 0;
    }
    if ((*sfl)->next == NULL)
    {
        r = (*sfl)->data;
        delete (*sfl);
        (*sfl) = NULL;
        return r;
    }
    while(pre_last->next)
    {
        pre_last = pre_last->next;
    }

    r = pre_last->data;
    pre_last = (*sfl);
    while(pre_last->next->next)
    {
        pre_last = pre_last->next;
    }
    delete pre_last->next;
    pre_last->next = NULL;
    return r;
}

bool push_forward(subforwardlist **sfl, int d)
{
    subforwardlist *tmp = new subforwardlist;
    tmp->data = d;
    tmp->next = *sfl;
    *sfl = tmp;
    return true;
}


int pop_forward(subforwardlist **sfl)
{
    int r=0;
    if ((*sfl) == NULL)
        return 0;
    r = (*sfl)->data;
    if ((*sfl)->next == NULL)
    {
        delete (*sfl);
        (*sfl) = NULL;
        return r;
    }
    subforwardlist *tmp = (*sfl)->next;
    delete (*sfl);
    (*sfl) = tmp;
    return r;
}

bool push_where(subforwardlist **sfl, unsigned int where, int d)
{
    subforwardlist *elem = new subforwardlist;
    subforwardlist *tmp = *sfl;
    elem->data = d;
    elem ->next =NULL;
    if (where==0)
    {
        push_forward(sfl, d);
        delete elem;
        return true;
    }

    for (unsigned int i=0;i<where-1;i++)
    {
        tmp = tmp->next;
    }
    if (tmp->next == NULL)
    {
        push_back(sfl, d);
        delete elem;
        return true;
    }

    elem->next = tmp->next;
    tmp->next = elem;
    return true;

}

int erase_where(subforwardlist **sfl, unsigned int where)
{
    int r =0;
    subforwardlist *tmp = *sfl;
    if (where==0)
    {
        pop_forward(sfl);
        return 0;
    }
    for (unsigned int i=0;i<where-1;i++)
    {
        tmp = tmp->next;
    }
    if (tmp->next == NULL)
    {
        r=tmp->data;
        pop_back(sfl);
        return r;
    }
    r= tmp->next->data;
    subforwardlist *tmp2 = tmp->next->next;
    delete tmp->next;
    tmp->next = tmp2;
    return r;
}

unsigned int size(subforwardlist  **sfl)
{
    subforwardlist *tmp_sfl = (*sfl);
    unsigned int counter=0;
    if ((*sfl)==NULL)
    {
        return 0;
    }
    if ((*sfl)->next==NULL)
    {
        return 1;
    }
    while ((tmp_sfl)->next)
    {
        (tmp_sfl) = (tmp_sfl)->next;
        counter+=1;
    }
    return counter+1;
}

void clear(subforwardlist  **sfl)
{
    if ((*sfl)==NULL) return;
    clear(&((*sfl)->next));
    delete ((*sfl));
    *sfl = NULL;
}

#include <iostream>
#include <random>
#include <chrono>
#include<cmath>
#include<vector>
#include <iomanip>
#include <fstream>
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
    std::ofstream out;
    out.open("data3.txt");
    out << std::fixed << std::setprecision(10);
    double start = 0;
    double finish = 0;
    int repeats = 1000;
    subforwardlist *sv;
            init(&sv);
    for (int n = 1; n<=10000; n++)
    {
        double time = 0;
        for (int i=0;i<repeats;i++)
        {

            start = get_time();
            //push_where(&sv, 0, i);
            push_back(&sv, i);
            finish = get_time();
            time += (finish-start);

        }
        out << n << ' ' << time/repeats << endl;
    }

    return 0;
}
