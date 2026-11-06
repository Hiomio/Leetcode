class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& q) {

        unordered_map<int, int> mp;
        vector<int> res(q.size(), 0);

        // Step 1: Sort logs according to timestamps
        sort(begin(logs), end(logs), [](vector<int>& a, vector<int>& b){
            return a[1] < b[1];
        });

        // Step 2: Convert queries into intervals
        // {startTime, endTime, originalIndex}
        vector<vector<int>> temp;

        for(int i = 0; i < q.size(); i++){
            temp.push_back({q[i] - x, q[i], i});
        }

        // Step 3: Sort queries according to starting time
        sort(begin(temp), end(temp));

        // Two pointers for sliding window
        int i = 0, j = 0;

        // Step 4: Process queries
        for(int k = 0; k < temp.size(); k++){

            int qst = temp[k][0];
            int qed = temp[k][1];
            int idx = temp[k][2];

            // Expand window
            while(j < logs.size() && logs[j][1] <= qed){
                mp[logs[j][0]]++;
                j++;
            }

            // Shrink window
            while(i < j && logs[i][1] < qst){

                mp[logs[i][0]]--;

                if(mp[logs[i][0]] == 0){
                    mp.erase(logs[i][0]);
                }

                i++;
            }

            // Count inactive servers
            res[idx] = n - mp.size();
        }

        return res;
    }
};