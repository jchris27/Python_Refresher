# global scope
name = "Jin"
count = 1

def another():
    # parent scope
    color = "blue"
    global count
    count += 1
    print(count)
    print(count)
    def greeting(name):
        nonlocal color
        color = "red"
        # local scope
        print(color)
        print(name)
    greeting("Dave")

another()