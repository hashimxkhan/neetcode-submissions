class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int total = 0;
        int cur = 11000;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] > cur) {
                total+= (prices[i] - cur);
            }
            cur = prices[i];
        }
        return total;
    }
};