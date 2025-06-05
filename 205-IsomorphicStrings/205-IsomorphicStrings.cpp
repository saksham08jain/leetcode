// Last updated: 5/6/2025, 11:08:47 pm
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int arr[128];
        bool used[128];
        int length=s.length();
        memset(arr, -1, sizeof(arr));//works only when setting value 0,-1
        memset(used, false, sizeof(used));
        bool ans=true;
        for(int i=0;i<length;i++)
        {
            int chr=(int)s[i];
            if (arr[chr]==-1  )
            {
                arr[chr]=(int)t[i];
                if (used[(int)t[i]])
                {
                    return false;
                }
                used[(int)t[i]]=true;
            }
            else
            {
               if(arr[chr]!=(int)t[i]) 
                {
                ans=false;
                break;
                }
            }

        }
        return ans;
    }
};