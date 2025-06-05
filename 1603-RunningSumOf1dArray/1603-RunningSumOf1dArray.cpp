// Last updated: 5/6/2025, 11:06:24 pm
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> out;
        int runsum=0;
        for (auto i = nums.cbegin(); i != nums.cend(); ++i)
        {   
            runsum+=*i;
            out.push_back(runsum);
        }
  return out;
    }
};