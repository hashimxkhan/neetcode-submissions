class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> sets(nums.begin(), nums.end());
        int best = 0;
        for (int i = 0; i < nums.size(); i++) {
            auto it = sets.find(nums[i] - 1);
            int cur = 0;
            if (it == sets.end()) {
                int val = nums[i];
                auto it = sets.find(val);
                while (it != sets.end()) {
                    cur++;
                    val++;
                    it = sets.find(val);
                }
                if (cur > best) {
                    best = cur;
                }
            }
        }
        return best;
    }
};
