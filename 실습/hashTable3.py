hash_table = list([ 0 for i in range(5) ])

def get_key(data):
    return hash(data)

def hash_fuc(key):
    return key % 5

def save_data_storage(data, value):
    key = get_key(data)
    hash_address = hash_fuc(key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_address] = [key, value]

def read_data(data):
    key = get_key(data)
    hash_address = hash_fuc(key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index][0] == key:
                return hash_table[index][1]
        return None
    else:
        return None

save_data_storage('K', '016-1234-5678')
save_data_storage('Robin', '019-4321-5678')
save_data_storage('Lee', '017-4132-5678')
save_data_storage('Jin', '011-342-5678')
save_data_storage('Yoon', '010-4353-3248')

print(read_data('K'))
print(read_data('Robin'))
print(read_data('Lee'))
print(read_data('Jin'))
print(read_data('Yoon'))

print(hash_table)
