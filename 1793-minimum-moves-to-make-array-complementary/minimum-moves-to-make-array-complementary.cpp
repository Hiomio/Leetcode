class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {

        vector<int> v(2 * limit + 2, 0);

        int n = nums.size();

        for (int i = 0; i < n / 2; i++) {

            int a = min(nums[i], nums[n - 1 - i]);
            int b = max(nums[i], nums[n - 1 - i]);

            v[2] += 2;

            v[a + 1] -= 1;

            v[a + b] -= 1;

            v[a + b + 1] += 1;

            v[limit + b + 1] += 1;
        }

        int minOp = INT_MAX;
        int currOp = 0;

        for (int i = 2; i <= 2 * limit; i++) {

            currOp += v[i];

            minOp = min(minOp, currOp);
        }

        return minOp;
    }
};