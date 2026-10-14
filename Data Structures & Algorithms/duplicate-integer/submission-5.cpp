class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dups;
        for (const auto& num : nums) {
            if (dups.contains(num)) {
                return true;
            }
            dups.insert(num);
        }
        return false;
    }
};