// Last updated: 5/6/2025, 11:09:38 pm
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool hasPathSum(struct TreeNode* root, int targetSum){
bool ans=0;
    
    if(root==NULL)
        return 0;
    int newReqdSum=targetSum-root->val;
    //cout<<newReqdSum<<'\t'<<ans<<'\n';
    if(newReqdSum==0 && root->right==NULL && root->left==NULL)
        return 1;
    if(root->left!=NULL)
    {
        ans=ans||
            hasPathSum(root->left,newReqdSum);
    }
    if(root->right!=NULL)
        ans =ans||  hasPathSum(root->right,newReqdSum);
    return ans;
}