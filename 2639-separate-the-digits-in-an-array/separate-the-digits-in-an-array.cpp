class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        int n=nums.size();
        vector<int> res;
        stack<int> st;
        for(int i=n-1;i>=0;i--){
            int temp=nums[i];
            while(temp>0){
                st.push(temp%10);
                temp/=10;
            }
        }
        while(!st.empty()){
            res.push_back(st.top());
            st.pop();
        }
        return res;
    }
};