/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool flag = true;
    int check(TreeNode* cur) {
        if (!cur) {
            return 0;
        }
        int left = 1 + check(cur->left);
        int right = 1 + check(cur->right);

        if (left - right > 1 || left - right < - 1) {
            flag = false;
        }
        return std::max(left, right);

    }
    bool isBalanced(TreeNode* root) {
        check(root);
        return flag;
        
    }
};
