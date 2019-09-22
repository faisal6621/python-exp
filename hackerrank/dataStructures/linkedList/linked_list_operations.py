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


def insertNodeAtPosition(head, data, position):
    item = head
    for i in range(position - 1):
        item = item.next

    tmp = item.next
    node = SinglyLinkedListNode(data)
    node.next = tmp
    item.next = node
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

    data = int(input('item to add: '))
    position = int(input('position: '))
    llist.head = insertNodeAtPosition(llist.head, data, position)
    printLinkedList(llist.head)
