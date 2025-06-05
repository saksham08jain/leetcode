// Last updated: 5/6/2025, 11:07:07 pm
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int pivot=-1;
        int runsum=0;
        int sum=0;
            for (auto i2 = nums.begin(); i2 != nums.end(); ++i2)
            {
        int ele=*i2;
        sum+=ele;
            }
    
    int count=0;
    int leftsum,rightsum;
    for (auto i = nums.begin(); i != nums.end(); ++i)
    {
                
        int ele=*i;
        count++;
        runsum+=ele;
        leftsum=runsum-ele;
        rightsum=sum-leftsum-ele;
        if (leftsum==rightsum)
        {
            pivot=count-1;
            break;
        }
                }
                return pivot;
    }
};