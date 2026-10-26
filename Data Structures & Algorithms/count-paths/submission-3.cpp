class Solution {
public:

    
    int dp(int i, int j, int m, int n, std::vector<int>& memo) {
        if (i == m - 1 && j == n - 1) {
            return 1;
        }
        if (i >= m || j >= n) {
            return 0;
        }
        int idx = i * n + j;
        if (memo[idx] != -1) {
            return memo[idx];
        }
        memo[idx] = dp(i+1, j, m, n, memo) + dp(i, j+1, m, n, memo);
        return memo[idx];
    }
    int uniquePaths(int m, int n) {
        std::vector<int> memo(m * n, -1);
        return dp(0,0, m, n, memo);
    }
};
