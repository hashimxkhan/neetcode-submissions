class Solution {
public:
    int calPoints(vector<string>& operations) {
        std::vector<int> stack;
        for (auto& op : operations) {
            if (op == "+") {
                int n = stack.size();
                stack.push_back(stack[n-1] + stack[n-2]);
            }
            else if (op == "C") {
                stack.pop_back();
            }
            else if (op == "D") {
                int dbl = stack.back() * 2;
                stack.push_back(dbl);
            } else {
                stack.push_back(std::stoi(op));
            }
        }
        int total = 0;
        while (!stack.empty()) {
            total += stack.back();
            stack.pop_back();
        }
        return total;
    }
};