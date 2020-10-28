hash_table = list([ 0 for i in range(5) ])

def get_key(data):
    return hash(data)

def hash_fuc(key):
    return key % 5

def save_data_storage(data, value):
    key = get_key(data)
    hash_address = hash_fuc(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([key, value])
    else:
        hash_table[hash_address] = [[key, value]]

def read_data(data):
    key = get_key(data)
    hash_address = hash_fuc(key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

save_data_storage('K', '016-1234-5678')
save_data_storage('Robin', '019-4321-5678')
save_data_storage('Lee', '017-4132-5678')

print(read_data('K'))
print(read_data('Robin'))
print(read_data('Lee'))

print(hash_table)

print(list([1, 2]))
print([[1, 2]])