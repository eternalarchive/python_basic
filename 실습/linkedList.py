class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMg:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        node = self.head
        if self.head == '':
            print('데이터가 없습니다.')
            return
        if node.data == data:
            temp = node
            del temp
            return
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
            

linked_list1 = NodeMg(0)
linked_list1.add(1)
linked_list1.desc()
print('*')
linked_list2 = NodeMg(0)

for data in range(1, 10):
    linked_list2.add(data)

linked_list2.desc()
linked_list2.delete(2)
linked_list2.desc()
linked_list2.delete(0)
linked_list2.delete(9)
linked_list2.desc()