class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
  if not head or m== n:
    return head
  
  root = start = ListNode(None)
  root.next = head
  
  # start end 지정
  for _ in range(m-1):
    start = start.next
  end = start.next

  for _ in range(n - m):
    tmp, start.next, end.next = start.next, end.next, end.next.next
    start.next.next = tmp

  return root.next