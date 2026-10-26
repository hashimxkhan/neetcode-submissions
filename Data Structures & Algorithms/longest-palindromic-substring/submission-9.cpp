class Solution {
public:
    string ret = "";
    int best = 0;
    void check(int i,int j, string &s) {
        if (i < 0 || j >= s.size()) {
            return;
        }
        if (s[i] == s[j]) {
            if (best < j - i + 1) {
                ret = s.substr(i, j - i + 1);
                best = j - i + 1;
            }
            j++;
            i--;
            check(i, j, s);
        }
    }

    string longestPalindrome(string s) {
        for (int i = 0; i < s.size(); i++) {
            check(i, i+1, &s);
            check(i,i,&s);
        }
        return ret;
    }
};
