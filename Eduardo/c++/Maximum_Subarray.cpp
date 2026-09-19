#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int presentSum = nums[0];
        int globalMax = nums[0];

        for (int i = 1; i < nums.size(); i++)
        {
            presentSum = max(nums[i], nums[i] + presentSum);

            globalMax = max(globalMax, presentSum);
        }

        return globalMax;
    }
};