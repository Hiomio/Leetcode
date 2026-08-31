# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_crit_idx = -1
        last_crit_idx = -1

        min_distance = math.inf

        prev = head
        curr = head.next
        nxt = head.next.next

        curr_idx = 1
        
        while nxt:

            is_local_max = curr.val > prev.val and curr.val > nxt.val
            is_local_min = curr.val < prev.val and curr.val < nxt.val
            
            if is_local_max or is_local_min:

                if first_crit_idx == -1:
                    first_crit_idx = curr_idx
                else:

                    min_distance = min(min_distance, curr_idx - last_crit_idx)

                last_crit_idx = curr_idx

            prev = curr
            curr = nxt
            nxt = nxt.next
            curr_idx += 1

        if first_crit_idx == last_crit_idx:
            return [-1, -1]

        max_distance = last_crit_idx - first_crit_idx
        
        return [min_distance, max_distance]
        