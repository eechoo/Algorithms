#include<vector>
#include<string>
#include<iostream>
using namespace std;
using std::vector;
using std::string;

class Solution {
public:
    int len;
    
    void nextPer(string &s)
    {
        char tmp;
        
        
        for(int i=len-2,j,k;i>=0;i--)
        {
            if(s[i]<s[i+1])
            {
                for(j=len-1;j>i;j--)
                {
                    if(s[j]>s[i])
                    {
                        swap(s[i],s[j]);
                        
                        for(k=1;i+2*k<=len;k++)
                        {
                            swap(s[i+k],s[len-k]);
                        }
                        
                        break;
                    }
                }

                cout<<i<<"/"<<j<<"/"<<k<<"/"<<endl;

                cout<<s<<endl;

                break;
            }
        }
    }
    
    string getPermutation(int n, int k) {
        string base(n,' ');
        
        len=n;
        
        for(int i=1;i<=n;i++)
        {
            base[i-1]='0'+i;
        }
        
        for(int i=1;i<k;i++)
        {
            nextPer(base);
        }
        
        return base;
    }
};

int main()
{
    Solution b;

    b.getPermutation(3,3);
}