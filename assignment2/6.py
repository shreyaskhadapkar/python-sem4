def valley(l):
    if (len(l) < 3):
        return False
 
    m = 1
    n = 1
 
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            if n > 1:
                return False
            m = m + 1
        if l[i] < l[i + 1]:
            n = n + 1
        if l[i] == l[i + 1]:
            return False
            
    if m > 1 and n > 1:
        return True
    else:
        return False
 
print(valley([3, 2, 8, 1, 2, 3]))