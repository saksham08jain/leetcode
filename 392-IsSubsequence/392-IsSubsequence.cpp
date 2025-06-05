// Last updated: 5/6/2025, 11:07:45 pm
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int l1=s.length();
        int l2=t.length();
        int p1=0;
        int p2=0;
        while(p1<s.length() & p2<t.length())
        {
            char chr1=s[p1];
            char chr2=t[p2];
            if(chr1!=chr2)
            {
                p2++;
            }
            else
            {
                p1++;
                p2++;
            }
        }
        if(p1==s.length())
            return true;
        return false;
    }
};