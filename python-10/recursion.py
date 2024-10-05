def add_one(num):

    if (num >= 9):
        return num + 1
    
    total = num + 1
    print(total)

    return add_one(total)

# mynewtotal = add_one(0)
# print(mynewtotal)

def loop_add_one(num):
    for x in range(num, 10):
        total = x
        print(total)
        if (x >= 9):
            return x+1

loop_total = loop_add_one(5)
print(loop_total)