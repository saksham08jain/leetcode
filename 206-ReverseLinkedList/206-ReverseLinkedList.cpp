// Last updated: 5/6/2025, 11:08:46 pm
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *curr; 
        ListNode *ans;
        curr=head;
        ans=NULL;
        while(curr!=NULL)
        {   //prev=curr;
            ans=new ListNode(curr->val,ans);
            curr=curr->next ;
           
            
            

        }
        return ans;
    }
};