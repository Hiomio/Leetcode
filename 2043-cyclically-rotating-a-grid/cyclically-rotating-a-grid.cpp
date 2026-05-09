class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int n=grid.size(),m=grid[0].size();
        int layers=min(n/2,m/2);
        for(int layer=0;layer<layers;layer++){
            int top=layer;
            int bottom=n-1-layer;
            int left=layer;
            int right=m-1-layer;
            vector<int>nums;
            for(int j=left;j<=right;j++) nums.emplace_back(grid[top][j]);
            for(int i=top+1;i<=bottom;i++) nums.emplace_back(grid[i][right]);
            for(int j=right-1;j>=left;j--) nums.emplace_back(grid[bottom][j]);
            for(int i=bottom-1;i>=top+1;i--) nums.emplace_back(grid[i][left]);
            int rot=k%(nums.size());
            reverse(nums.begin(),nums.begin()+rot);
            reverse(nums.begin()+rot,nums.end());
            reverse(nums.begin(),nums.end());
            int idx=0;
            for(int j=left;j<=right;j++){
                grid[top][j]=nums[idx];
                idx++;
            }
            for(int i=top+1;i<=bottom;i++){
                grid[i][right]=nums[idx];
                idx++;
            }
            for(int j=right-1;j>=left;j--){
                grid[bottom][j]=nums[idx];
                idx++;
            }
            for(int i=bottom-1;i>=top+1;i--){
                grid[i][left]=nums[idx];
                idx++;
            }
        }
        return grid;
    }
};
