
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums: list[int] = []

        self.fill_nums(head, nums)

        size: int = len(nums)
        maxi: int = 0
        for i in range(0, size // 2):
            sum_: int = nums[i] + nums[size -i -1]
            maxi = max(maxi, sum_)

        return maxi

    def fill_nums(self, head: ListNode, nums: list[int]) -> None:
        while head is not None:
            nums.append(head.val)
            head = head.next