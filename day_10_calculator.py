def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}


def calculator():
    flag = True
    n1 = float(input("Enter 1st number: "))

    while flag:
        operation = input("Enter operation you want to perform +, -, * or /: ")
        n2 = float(input("Enter 2nd number: "))
        answer = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start again")
        if choice == 'y':
            n1 = answer
        else:
            flag = False
            print("\n" * 20)
            calculator()


calculator()
