// Last updated: 5/6/2025, 11:10:35 pm
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
    ListNode* ans;
    ListNode* curr;

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list2==NULL )
            return list1;
        if(list1==NULL)
            return list2;
        
        
        if(list1->val>list2->val)
        {
            ans= new ListNode(list2->val);
            list2=list2->next;
        }
        else
        {
            ans=new ListNode(list1->val);
            list1=list1->next;
        }
        curr=ans;
        
        while(list1 !=NULL | list2!=NULL)
        {
            if(list1==NULL )
            {
                curr->next=new ListNode(list2->val);
                curr=curr->next;
                list2=list2->next;
                continue;
            }
                if(list2==NULL )
            {
                curr->next=new ListNode(list1->val);
                curr=curr->next;
                list1=list1->next;
                continue;
            }
                    if(list1->val>list2->val)
        {
            curr->next=new ListNode(list2->val);
            curr=curr->next;
            list2=list2->next;
        }
        else
        {
            (curr->next)=new ListNode(list1->val);
            curr=curr->next;
            list1=list1->next;
        }

        }
        
    return ans;
    }
};