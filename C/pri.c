#include<vector>
#include<string>

using namespace std;
using std::vector;
using std::string;

class Solution {
public:
    int minCut(string s) {
        int len = s.size();
        vector<vector<int> > pal(len,vector<int>(len,0));
        vector<int> count(len+1,0);
        int minT;
        
        for(int i=0;i<len;i++)
        {
            pal[i][i]=1;
        }
        
        for(int i=len-1;i>=0;i--)
        {
            for(int j=i;j<len;j++)
            {
                if(i==j)
                    pal[i][j]=1;
                    
                if(s[i]==s[j])
                {
                    if(i+1==j)
                        pal[i][j]=1;
                    
                    if(i+2<=j&&pal[i+1][j-1]==1)
                        pal[i][j]=1;
                }
            }
        }

        for(int i=0;i<len;i++)
        {
            for(int j=0;j<len;j++)
            {
                printf("%d",pal[i][j]);
            }

            printf("\n");
        }

        printf("\n");
        
        for(int i=len-1;i>=0;i--)
        {   // c[i,m] +1 + c[m+1,j]
            count[i]=65550;
            
            for(int j=i;j<len;j++)
            {
                if(pal[i][j]==1)
                    count[i]=min(count[j+1]+1,count[i]);
            }
        }
        
        return count[0]-1;
    }
};

int main()
{
    Solution b;

    printf("ret=%d\n",b.minCut("a"));

    return 1;
}