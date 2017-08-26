items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(items):
    if not (item % 2):
        items[index] = None
print(items)