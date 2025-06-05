// Last updated: 5/6/2025, 11:08:02 pm
class Solution {
public:
    int minPatches(vector<int>& coins, int target) {
        long long curreq =1;
        long long i=0;
        long long n =coins.size();
        // sort(coins.begin(),coins.end());
        long long ans =0;
        while (i<n && curreq<=target) {
            if (coins[i]<=curreq) {
                curreq += coins[i];
                i++;
            }
            else {
                ans++;
                curreq += curreq;
            }
        }
        if (i>=n) {
            while (curreq<=target) {
                ans++;
                curreq+= curreq;
            }

        }
        return ans;
    }
};