class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def insert_at_first(self,head,x):
        new_node = Node(x)
        new_node.next = head
        head = new_node
        return head

    def insert_at_last(self,head,x):
        new_node = Node(x)
        if head is None:
            return new_node
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head

    def insert_at_mid(self,head,x):
        new_node = Node(x)
        if head is None:
            return new_node
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = new_node
        new_node.next = slow
        return head


    def print(self,head):
        current = head
        while current is not None:
            print(current.data)
            current = current.next

linked_list = LinkedList()
head = None
head = linked_list.insert_at_first(head,10)
head = linked_list.insert_at_first(head,20)
head = linked_list.insert_at_first(head,30)

head = linked_list.insert_at_last(head,40)
head = linked_list.insert_at_mid(head,15)

linked_list.print(head)