class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    max_len, len1, len2 = 0, 0, 0

    current1 = l1.copy()
    current2 = l2.copy()

    while l1.next != None:
        current1 = current1.next
        len1 += 1

    while l2.next != None:
        current2 = current2.next
        len2 += 1
    
    max_len = max(len1, len2)
    print(max_len)