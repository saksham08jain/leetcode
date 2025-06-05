// Last updated: 5/6/2025, 11:06:12 pm
class Solution {
public:
    int minimumAddedCoins(vector<int>& coins, int target) {     
        int curreq =1;
        int i=0;
        int n =coins.size();
        sort(coins.begin(),coins.end());
        int ans =0;
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