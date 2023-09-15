#Arrays and Lists

#Binary search
def binary_search(arr, n):
    if not arr:
        return False
    if len(arr) == 1:
        return True if arr[0] == n else False
    x = len(arr) // 2 
    if arr[x] > n:
        return binary_search(arr[:x], n)
    elif arr[x] < n:
        return binary_search(arr[x:], n)
    return True

#Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        return [min(arr), max(arr)]
    return merge(merge_sort(arr[:len(arr) // 2]), merge_sort(arr[len(arr) // 2:]))

def merge(a1, a2):
    i, j, arr = 0, 0, []
    while True:
        if  i >= len(a1):
            arr += a2[j:]
            break
        elif j >= len(a2):
            arr += a1[i:]
            break
        if a1[i] < a2[j]:
            arr.append(a1[i])
            i += 1
        else:
            arr.append(a2[j])
            j += 1
    return arr

#Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    a1 = []
    a2 = []
    for i in arr[1:]:
        if i < arr[0]:
            a1.append(i)
        elif i > arr[0]:
            a2.append(i)
    return quick_sort(a1) + [arr[0]] + quick_sort(a2)

#Sliding window example
def norepeats(arr):
    i, j, m, l = 0, 0, 0, []
    while i < len(arr):
        m = max(m, len(l))
        while arr[i] in l:
            l = l[1:]
        l.append(arr[i])
        i += 1
    m = max(m, len(l))
    return m

#Linked Lists
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedList:
    def __init__(self, head):
        self.head = ListNode(head)
        
    def __getitem__(self, k):
        i = -1
        cur = self.head
        while cur:
            if i == k:
                return cur.val
            cur = cur.next
            i += 1
        raise IndexError("Linked List index out of range")

    def __repr__(self):
        l = []
        cur = self.head
        while cur:
            l.append(str(cur.val))
            cur = cur.next
        return ' -> '.join(l)
    
    def append(self, val):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def insert(self, k, val):
        i = -1
        cur = self.head
        while cur:
            if i == k:
                node = ListNode(val)
                node.next = cur.next
                cur.next = node
                return
            cur = cur.next
            i += 1
        raise IndexError("Linked List index out of range")

    def delete(self, k):
        i = 0
        cur = self.head
        while cur:
            if i == k:
                try:
                    cur.next = cur.next.next
                except:
                    cur.next = None
                return
            cur = cur.next
            i += 1
        raise IndexError("Linked List index out of range")

#Stacks
class stack:
    def __init__(self):
        self.stack = []
    def __repr__(self):
        return'\n'.join(self.stack[::-1])
    def __getitem__(self, k):
        try:
            return self.stack[k]
        except:
            raise IndexError("Stack index out of range")
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

#Quenes
class quene:
    def __init__(self):
        self.quene = []
    def __repr__(self):
        return' '.join(self.quene)
    def __getitem__(self, k):
        try:
            return self.quene[k]
        except:
            raise IndexError("Quene index out of range")
    def enquene(self, val):
        self.quene.append(val)
    def dequene(self):
        return self.stack.pop(0)








            