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
    ListNode* rotateRight(ListNode* head, int k) {
        if(!head || !head->next) return head;

        ListNode* tail = head;
        int len = 1;

        // Find length and last node
        while(tail->next != nullptr){
            len++;
            tail = tail->next;
        }

        // Optimize k
        k = k % len;
        if(k == 0) return head;

        // Make circular
        tail->next = head;

        // Find new tail
        ListNode* temp = head;
        for(int i = 1; i < len - k; i++){
            temp = temp->next;
        }

        // Set new head
        ListNode* newHead = temp->next;

        // Break the circle
        temp->next = nullptr;

        return newHead;
    }
};
