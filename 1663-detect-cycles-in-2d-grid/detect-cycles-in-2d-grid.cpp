class Solution {
public:
    bool bfs(vector<vector<int>>&vis,vector<vector<char>>& grid,int x,int y)
    {
        int m = grid.size();
        int n = grid[0].size();

        queue<pair<pair<int,int>,pair<int,int>>>q;
        q.push({{x,y},{-1,-1}});
        vis[x][y]=1;

        int dx[4] = {1,-1,0,0};
        int dy[4] = {0,0,1,-1};

        while(!q.empty())
        {
            auto[cc,p] = q.front();
            int r = cc.first;
            int c = cc.second;

            q.pop();

            for(int d=0;d<4;++d)
            {
                int nr = r+dx[d];
                int nc = c+dy[d];

                if(nr<0 || nc<0 || nr>=m || nc>=n ||(nr==p.first&&nc==p.second)  || grid[nr][nc]!=grid[r][c])continue;

                if(vis[nr][nc] && nr!=p.first && nc!=p.second)return true;

                vis[nr][nc]=1;
                q.push({{nr,nc},{r,c}});
            }
        }
        return false;
    }
    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>>vis(m,vector<int>(n,0));

        for(int i=0;i<m;++i)
        {
            for(int j=0;j<n;++j)
            {
                if(!vis[i][j])
                {
                    bool ok = bfs(vis,grid,i,j);
                    if(ok)return true;
                }
            }
        }
        return false;
    }
};