my_list = [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(my_list):
    my_list = set(my_list)
    return list(my_list)
print(unique_list(my_list))