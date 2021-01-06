lst = [6, 3, 2, 2, 4, 3, 4]
max_size = 12
lst.sort(reverse=True)
print(f'original list: {lst}')

def matchy_round():
    tmp_lst = list()

    while len(lst) > 0 or sum(tmp_lst) != max_size:
        for item in lst:
            if item + sum(tmp_lst) < max_size:
                tmp_lst.append(item)
            elif item + sum(tmp_lst) == max_size:
                tmp_lst.append(item)
                break
        break
    for value in tmp_lst:
        if value in lst:
            lst.remove(value)

    return tmp_lst

print(f'matchy_round: {matchy_round()}')
print(f'list after matchy round: {lst}')

#work in progress