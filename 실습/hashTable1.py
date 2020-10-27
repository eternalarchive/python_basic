hash_table = list([0 for i in range(0, 10)])

def hash_fuc(key):
    return key % 5

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_fuc(key)
    hash_table[hash_address] = value

def get_value(data):
    key = ord(data[0])
    hash_address = hash_fuc(key)
    return hash_table[hash_address]

storage_data('Andy', '010-1234-5678')
storage_data('Lilly', '010-4321-5678')
storage_data('Jin', '010-4132-5678')

print(get_value('Andy'))
print(get_value('Lilly'))
print(get_value('Jin'))

print(hash_table)

hash_table2 = list([ 0 for i in range(8) ])

def get_key(data):
    return hash(data)

def hash_fuc2(key):
    return key % 8

def save_data_storage(data, value):
    key = get_key(data)
    hash_address = hash_fuc2(key)
    hash_table2[hash_address] = value

def read_data(data):
    key = get_key(data)
    hash_address = hash_fuc2(key)
    return hash_table2[hash_address]

save_data_storage('K', '016-1234-5678')
save_data_storage('Hyun', '019-4321-5678')
save_data_storage('Robin', '017-4132-5678')

print(read_data('K'))
print(read_data('Hyun'))
print(read_data('Robin'))

print(hash_table2)