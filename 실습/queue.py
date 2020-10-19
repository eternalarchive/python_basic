queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(0, 10):
    enqueue(index)

print(queue_list)
dequeue()
print(queue_list)