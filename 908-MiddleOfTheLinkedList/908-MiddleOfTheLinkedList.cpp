// Last updated: 5/6/2025, 11:06:45 pm
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
    ListNode* middleNode(ListNode* head) {
        if(head==NULL)
            return NULL;
        ListNode *fastptr;
        fastptr=head;
        ListNode *slowptr;
        slowptr=head;
        while(fastptr!=NULL && fastptr->next!=NULL )
        {
            slowptr=slowptr->next;
            fastptr=fastptr->next->next;
        }
        return slowptr;
    }
};