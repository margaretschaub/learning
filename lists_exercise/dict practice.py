list_1 = [1,1,3,4,5,1,4,2,7,8,2,9,10,10,11,35,567,234,3,23,11]


def using_set(list):
    new_set =set(list)
    return new_set


def using_for_loop(list):
    new_list = []
    for item in list:
        if item not in new_list:
           new_list.append(item)
    return new_list


def using_for_loop_alternate(list):
    new_set = set()
    for item in list:
            new_set.add(item)
    return new_set

def making_a_dict(list):
    """this is a helpfule meda"""
    x = list
    y = 0
    this_dict = dict.fromkeys(x,y)
    return this_dict

print(using_set(list_1))
print(using_for_loop(list_1))
print(using_for_loop_alternate(list_1))
print(making_a_dict(list_1))

#Look into unit tests
# Nosetests

#should I sort?
#should I convert dict to a set (no values)