class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMg:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            new.prev = node
            node.next = new
            self.tail = new

    def desc(self):
        if self.head == None:
            print('데이터가 없습니다')
            return
        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next
            
    def search_from_head(self, data):
        if self.head == None:
            print('데이터가 없습니다.')
            return
        else:
            node = self.head
            while node:
                if node.data == data:
                    return data
                else:
                    node = node.next
            return print('해당하는 데이터가 존재하지 않습니다.')

    def search_from_tail(self, data):
        if self.head == None:
            return print('데이터가 없습니다')
        else:
            node = self.tail
            while node:
                if node.data == data:
                    return data
                else:
                    node = node.prev
            return print('해당하는 데이터가 존재하지 않습니다.')

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            before_node = node.prev
            new = Node(data)
            new.prev = before_node
            new.next = node
            before_node.next = new
            node.prev = new

double_linked_list = NodeMg(0)
double_linked_list.desc()

for index in range(1, 10):
    double_linked_list.insert(index)

double_linked_list.desc()
print(double_linked_list.search_from_head(3))

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()