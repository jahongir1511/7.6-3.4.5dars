#  misol linki   https://www.codewars.com/kata/59557b2a6e595316ab000046/train/python


def convert_hash_to_array(hash):
    return [[key, value] for key, value in hash.items()]

hash_example = {'name': 'Jeremy', 'age': 24, 'role': 'Software Engineer'}
result = convert_hash_to_array(hash_example)
print(result)
