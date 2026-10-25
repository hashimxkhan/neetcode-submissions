class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        int min = 101;
        for (auto& price : prices) {
            if (price < min) {
                min = price;
            }
            else {
                best = std::max(best, price - min);
            }
        }
        return best;
    }
};
