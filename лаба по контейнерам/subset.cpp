#include <iostream>
using std::cout;
using std::endl;
struct subset_node {
    int key;
    subset_node *left;
    subset_node *right;
};
bool init(subset_node **sn)
{
    *sn = NULL;
    return true;
}
unsigned int height1(subset_node *sn, int h)
{
    subset_node *root = sn;
    if (sn==NULL)
        return 0;
    if (root->left == NULL && root->right == NULL)
    {
        h+=1;
        return h;
    }
    h+=height1(root->left,1);
    h+=height1(root->right,1);
    return h;
}
unsigned int height(subset_node *sn)
{
    return height1(sn,0);
}
bool insert(subset_node **sn, int k)
{
    subset_node *elem = new subset_node;
    elem -> key = k;
    elem -> right = NULL;
    elem -> left = NULL;
    if ((*sn) == NULL)
    {
        *sn = elem;
        return true;
    }
    subset_node *root = *sn;
    while (root)
    {
        if (root->key == k)
            {
                delete elem;
                return false;
            }
        if (root->key>k)
        {
            if (root->left == NULL)
            {
                root->left = elem;
                return true;
            }
            root = root->left;
            continue;
        }
        if (root->key<k)
        {
            if (root->right == NULL)
            {
                root->right = elem;
                return true;
            }
            root = root->right;
        }
    }
    delete elem;
    return false;
}
unsigned int size(subset_node *sn)
{
    if (sn==NULL) return 0;
    return size(sn->left)+size(sn->right)+1;
}
subset_node* find(subset_node *sn, int k)
{
    if (sn == NULL)
        return NULL;
    subset_node *root = sn;
    while (root)
    {
        if (root ->key == k)
            return root;
        if (root->key>k)
        {
            if (root->left == NULL)
            {
                return NULL;
            }
            root = root->left;
        }
        else
        {
            if (root->right == NULL)
            {
                return NULL;
            }
            root = root->right;
        }
    }
    return NULL;
}
int * DFS(subset_node *sn)
{
    if (sn==NULL)
    {
        return NULL;
    }
    int l = size((sn->left));
    int r = size(sn->right);
    int *arr = new int [l+r+1];
    if (l>0)
    {
        int *arrL = DFS(sn->left);
        for (int i=0;i<l;i++)
        {
            arr[i] = arrL[i];
        }
        delete[] arrL;
    }
    arr[l] = sn->key;
    if (r>0)
    {
        int *arrR = DFS(sn->right);
        for (int i=0;i<r;i++)
        {
            arr[i+l+1] = arrR[i];
        }
        delete[] arrR;
    }
    return arr;
}

void destructor(subset_node **sn)
{
    if ((*sn) == NULL) return;
    destructor(&((*sn)->left));
    destructor(&((*sn)->right));
    delete ((*sn));
    *sn = NULL;
}
subset_node* findMin(subset_node* sn)
{
    if (sn->left == NULL)
    {
        return sn;
    }
    return findMin(sn->left);
}
bool remove(subset_node **sn, int k) {
    if (*sn == NULL) return true;
    if ((*sn)->key < k) {
        remove(&((*sn)->right), k);
    }
    else if ((*sn)->key > k) {
        remove(&((*sn)->left), k);
    }
    else {
        if ((*sn)->left == NULL) {
            subset_node *tmp = *sn;
            *sn = (*sn)->right;
            delete tmp;
        }
        else if ((*sn)->right == NULL) {
            subset_node *tmp = *sn;
            *sn = (*sn)->left;
            delete tmp;
        }
        else {
            subset_node *tmp = findMin((*sn)->right);
            (*sn)->key = tmp->key;
            remove(&((*sn)->right), tmp->key);
        }
    }
    return true;
}





#include <random>
#include <chrono>
#include <climits>

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

    return 0;
}


