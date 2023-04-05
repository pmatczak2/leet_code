# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == "__main__":

    if __name__ == "__main__":
        app = Solution()

        # create linked lists
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        # call method with linked lists
        result = app.addTwoNumbers(l1, l2)

        # print output
        while result:
            print(result.val, end='')
            result = result.next

# line 19-22 This block of code defines a class ListNode that represents a single node in a singly-linked list.
# Each node has two attributes: val (which stores the value of the node) and next (which points to the next node
# in the list).

# line 25-28 This block of code defines a class Solution that has a method addTwoNumbers which takes in two linked
# lists l1 and l2 as arguments and returns a new linked list that represents the sum of the two input linked lists.
# This block of code creates a new ListNode object called dummy with default values for val and next, and then creates a
# new variable cur that initially points to the dummy node. dummy serves as a placeholder that helps us keep track of
# he head of the result linked list

# Line 30-33 This block of code initializes a variable carry to 0, and then starts a while loop that will run until
# we have finished processing all the nodes in both input linked lists as well as any carry-over from the previous
# addition operation. This block of code creates two new variables v1 and v2 that store the values of the current
# nodes in l1 and l2, respectively. If l1 or l2 is None, which means we have reached the end of the linked list,
# we set the value to 0. l1 is a reference to a ListNode object. If l1 is not None (i.e., l1 is a valid ListNode
# object), then v1 is assigned the value of l1.val. If l1 is None (i.e., there is no more node to process),
# then v1 is assigned the value of 0. So, in other words, this line of code is assigning the value of l1.val to v1 if
# l1 is not None, and assigning the value of 0 to v1 if l1 is None.

# line 36-39 This block of code computes the sum of v1, v2, and the carry-over from the previous addition operation (
# which is initially 0). We then update the carry variable to be the integer division of val by 10, and we update val
# to be the remainder of val divided by 10. This way, val will always be a single-digit number. val = v1 + v2 +
# carry: The sum of the current digits from l1 and l2 (as well as any carry from the previous sum) is calculated and
# assigned to val.
#
# carry = val // 10: If the sum val is greater than or equal to 10, then there is a carry that needs to be added to
# the next sum. This carry is calculated by taking the integer division of val by 10, which gives us the carry value
# of either 0 or 1.
#
# val = val % 10: The new digit to be added to the result linked list is obtained by taking the remainder of val
# divided by 10. This gives us the value of the current digit in the ones place, which is what we want to add to the
# result linked list.
#
# Overall, these three lines of code are taking two digits (one from l1 and one from l2) along with any carry from
# the previous sum, adding them up, and producing the appropriate new digit to add to the result linked list,
# as well as the carry value for the next iteration.
#
# A new ListNode object is created and assigned to cur.next. The value of the new ListNode object is val,
# which is the sum of the corresponding digits in l1 and l2, plus any carry from the previous digit. The next
# attribute of the new ListNode object is initially None.
#
# 'cur' points to the last ListNode object that was created, and 'cur.next' is set to the new ListNode object,
# effectively linking the new node to the previous node in the linked list. After this, cur is updated to point to
# the newly created node so that the next node can be added to the list.

# line 42 This block of code creates a new ListNode object with the value val, and sets the next attribute of cur
# (which initially points to dummy) to point to the new node. We then update cur to point to the new node, so that we
# can add more nodes to the linked list as necessary.

# Line 43-44 This block of code updates the pointers to the next nodes in the input linked lists l1 and l2. If we
# have reached the end of the linked list (i.e., l1 or l2 is None), we set the pointer to None. If l1 is not None,
# l1 = l1.next moves the l1 pointer to the next node in the linked list. If l1 is None, l1 = None simply sets l1 to
# None, indicating that there are no more nodes to traverse in the linked list.
#
# Similarly, if l2 is not None, l2 = l2.next moves the l2 pointer to the next node in the linked list. If l2 is None,
# l2 = None simply sets l2 to None, indicating that there are no more nodes to traverse in the linked list.
#
# These two lines are important because they allow the loop to continue iterating through the linked lists until
# there are no more nodes to process, ensuring that all the digits in both numbers are added together.

# line 46: Finally, this block of code returns the next node of dummy, which is the first node in the result linked
# list (since dummy is a placeholder node)