class Solution {
public:
    std::unordered_map<int, int> cache_false;
    std::unordered_map<int, int> cache_true;

    int dp(int i, bool first, vector<int>& nums) {
        if (i >= nums.size()) {
            return 0;
        }
        if (i == nums.size() - 1) {
            return first ? 0 : nums[i];
        }
        if (first) {
            if (cache_true.contains(i)) {
                return cache_true[i];
            }
            cache_true[i] = std::max(nums[i] + dp(i+2, first, nums),dp(i+1, first, nums));
            return cache_true[i];
        } else {
            if (cache_false.contains(i)) {
                return cache_false[i];
            }
            cache_false[i] = std::max(nums[i] + dp(i+2, first, nums),dp(i+1, first, nums));
            return cache_false[i];
        }

    }

    int rob(vector<int>& nums) {
        return std::max(dp(0, true, nums), dp(1, false, nums));
    }
};
