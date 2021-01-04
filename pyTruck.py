max_load = float(input('What is the maximum carry load of the truck:  '))
boxes = list()
load = list()

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
    if box > max_load:
        print('We\'re gonna need a bigger truck!\nCannot add item')
        continue
    if box > 0.0:
        boxes.append(box)
    elif box <= 0.0:
        print('Not a valid value\nCannot add item')

boxes.sort()
print(f'\nMax carry load: {max_load}, items: {boxes}\n')

# trys to greedy add largest array first from largest to smallest weights
# if sum of array is more than max load then function will try a smaller array with lightest item removed first
def add_load(max_load, boxes):
    add_load = []
    temp_load = []
    for i in range(0,len(boxes)):
        if sum(boxes[i:]) <= max_load:
            add_load.append(boxes[i:])
            break
    print(add_load)
    return add_load

# start add load function and remove corresponding item from boxes
def remove_boxes():
    removed_boxes = add_load(max_load, boxes)
    removed_boxes = (removed_boxes[0])
    for item in removed_boxes:
        boxes.remove(item)
    return boxes

# main function wrapper, while there are boxes remove largest array and increase count
def load_count():
    count = 0
    while boxes:
        remove_boxes()
        count += 1
    return count

print(f'Amount of times to load truck:  {load_count()}')

# need to iterate not just with adjacent value but all remaining values, not true greedy algorithm
# change add load function
