// Last updated: 5/6/2025, 11:09:20 pm
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slowptr=head;
        ListNode *fastptr=head;

        while(1)
        {
            if(fastptr==NULL or fastptr->next==NULL)
            {
                return NULL;
            }
            slowptr=slowptr->next;
            fastptr=fastptr->next->next;
            if(slowptr==fastptr)
                break;
        }
        // cout<<fastptr->val<<endl;
        // cout<<slowptr->val<<endl;
        slowptr=head;
        while(slowptr!=fastptr)
        {
            slowptr=slowptr->next;
            fastptr=fastptr->next;
        }
        //cout<<fastptr->val;
       // cout<<slowptr->val;
        return fastptr;
    }
};