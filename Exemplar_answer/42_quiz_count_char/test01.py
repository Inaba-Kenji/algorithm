max_value = None
max_item = None
l = [('t', 2), ('h', 2), ('i', 4), ('s', 4), ('i', 4), ('s', 4), ('a', 4), ('p', 6), ('e', 4), ('n', 3), ('.', 3), ('t', 2), ('h', 2), ('i', 4), ('s', 4), ('i', 4), ('s', 4), ('a', 4), ('n', 3), ('a', 4), ('p', 6), ('p', 6), ('l', 2), ('e', 4), ('.', 3), ('a', 4), ('p', 6), ('p', 6), ('l', 2), ('e', 4), ('p', 6), ('e', 4), ('n', 3), ('.', 3)]

for item in l:
    if max_value is None or item[1] > max_value:
        max_value = item[1]
        max_item = item
print(max_item)
