class Solution {
public:
        std::unordered_map<int, int> cache;
        int dp(int i, vector<int>& nums) {
            if (i >= nums.size()) {
                return 0;
            }
            if (cache.contains(i)) {
                return cache[i];
            }
            int cur = 1;
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[j] > nums[i]) {
                    cur = std::max(1 + dp(j, nums), cur);
                }
            }
            cache[i] = cur;
            return cur;
        }

    int lengthOfLIS(vector<int>& nums) {

        int best = 0;
        for (int i = 0; i < nums.size(); i++) {
            best = std::max(dp(i, nums), best);
        }
        return best;
    }
};
