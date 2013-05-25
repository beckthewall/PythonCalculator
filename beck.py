import sys
# Beck's program



print "Welcome to the calculator"

while True:
    operation = raw_input("[c] count, [g]rid, [a]dd, [s]ubtract, [d]ivide, [m]ultiply, e[x]it? ")
    if operation in ["c", "g", "a", "s", "d", "m", "x"]:
        if operation == "x":
            sys.exit()
        first = int(raw_input("first number? "))
        second = int(raw_input("second number? "))
        answer = 0
        if operation == "a":
            answer = first + second
        elif operation == "s":
            answer = first - second
        elif operation == "d":
            answer = first / second
        elif operation == "m":
            answer = first * second
        elif operation == "g":
            for col in range(1, second+1):
                print "#" * first
        elif operation == "c":
            for col in range(1, second+1):
                answer = answer + first
        if operation <> "g":                          
            print "answer: "+str(answer)
    else:
        print "Invalid operation, try again..."



