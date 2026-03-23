def search (list,key):
    for i in range (len(list)):
        if list[i] == key:
            return i
    return -1