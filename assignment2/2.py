def matched(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count == 0:
        print(True)
        return True
    else:
        print(False)
        return False
 
s = ("Hey , I'm from INFT(D10)")
matched(s)

s = "(shreyas ()"
matched(s)