class Solution {
public:
    int rotatedDigits(int n) {
        int ans =0;
        for(int i=1;i<=n;i++){
            unordered_map<int,int> mpp;
            int temp = i;
            while(temp>0){
                mpp[temp%10]++;
                temp /= 10;
            }

            if(mpp.count(4) || mpp.count(3) || mpp.count(7)){
                continue;
            }

            if(mpp.count(2) || mpp.count(5) || mpp.count(6) || mpp.count(9)){
                ans++;
            }
        }

        return ans;
    }
};