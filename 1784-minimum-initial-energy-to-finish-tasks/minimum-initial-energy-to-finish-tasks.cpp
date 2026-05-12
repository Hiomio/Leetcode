class Solution {
    static bool cmp(vector<int>& a, vector<int>& b) {
        return (a[1] - a[0]) > (b[1] - b[0]);
    }

public:
    int minimumEffort(vector<vector<int>>& tasks) {

        sort(tasks.begin(), tasks.end(), cmp);

        int current = 0;
        int extra = 0;

        for (auto& temp : tasks) {

            if (current < temp[1]) {

                extra += (temp[1] - current);

                current = temp[1];
            }

            current -= temp[0];
        }

        return extra;
    }
};