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
        cache[i] = std::max(nums[i] + dp(i+2, nums), dp(i+1, nums));
        return cache[i];
    }

    int rob(vector<int>& nums) {
        return dp(0, nums);

    }
};
