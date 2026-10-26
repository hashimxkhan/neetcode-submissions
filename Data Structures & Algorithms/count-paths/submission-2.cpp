class Solution {
public:

    int total = 0;
    
    void dp(int i, int j, int m, int n, std::vector<int>& memo) {
        if (i == m - 1 && j == n - 1) {
            total++;
            return;
        }
        if (i >= m || j >= n) {
            return;
        }
        dp(i+1, j, m, n, memo);
        dp(i, j+1, m, n, memo);
    }
    int uniquePaths(int m, int n) {
        std::vector<int> memo;
        dp(0,0, m, n, memo);
        return total;
    }
};
