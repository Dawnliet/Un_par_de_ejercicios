#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        int maxim = nums[0];
        int minp = nums[0];
        int maxp = nums[0];

        for (int i = 1; i < nums.size(); i++)
        {
            int num = nums[i];

            if (num < 0)
            {
                int temp = maxp;
                maxp = minp;
                minp = temp;
            }

            maxp = max(num, num * maxp);
            minp = min(num, num * minp);

            maxim = max(maxim, maxp);
        }

        return maxim;
    }
};