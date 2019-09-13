from hackerrank.dataStructures.linkedList.SinglyLinkedList import SinglyLinkedList, SinglyLinkedListNode


def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    if not head:
        head = new_node
        return head

    tail = head
    while tail.next:
        tail = tail.next
    tail.next = new_node
    return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
    data = input('item to add at tail: ')
    llist.head = insertNodeAtTail(llist.head, data)
    printLinkedList(llist.head)
