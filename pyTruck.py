max_load = float(input('What is the maximum carry load of the truck:  '))
boxes = list()

# asks for valid inputfor max load and weight of each item to load
while True:
    box = (input('Enter box load in weight [Enter \'done\' when finished]:  '))
    if box.lower() == 'done':
        break
    elif box == '':
        continue
    try:
        box = float(box)
    except ValueError:
        print('Please input a valid number value')
        continue
    if box > max_load:
        print('We\'re gonna need a bigger truck!\nCannot add item')
        continue
    if box > 0.0:
        boxes.append(box)
    elif box <= 0.0:
        print('Not a valid value\nCannot add item')

# test values
# boxes = [12, 6, 6, 2, 4, 3, 4, 1, 3]
# max_load = 12

boxes.sort(reverse=True)
print(f'\nMax carry load: {max_load}, items: {boxes}\n')

#greedy matches and then adds load
def add_load():
    tmp_boxes = list()
    
    while len(boxes) > 0 or sum(tmp_boxes) != max_load:
        for item in boxes:
            if item + sum(tmp_boxes) < max_load:
                tmp_boxes.append(item)
            elif item + sum(tmp_boxes) == max_load:
                tmp_boxes.append(item)
                break
        break
    for value in tmp_boxes:
        if value in boxes:
            boxes.remove(value)

    return tmp_boxes


# main function wrapper, while there are boxes remove largest array and increase count
def load_count():
    count = 0

    while len(boxes) > 0:
        print(add_load())
        count += 1

    # print(count)
    return count


print(f'Amount of times to load truck:  {load_count()}')