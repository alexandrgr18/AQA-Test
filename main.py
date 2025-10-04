# main.py

def check_number(num):
    if num > 7:
        print("Hello")

def check_name(name):
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def multiples_of_three(arr):
    print("Array elements that are multiples of 3:")
    for x in arr:
        if x % 3 == 0:
            print(x, end=" ")
    print()

def check_brackets(seq):
    stack = []
    pairs = {')':'(', ']':'['}
    for ch in seq:
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        check_number(num)
    except:
        print("Invalid number input")

    name = input("Enter a name: ")
    check_name(name)

    try:
        arr = list(map(int, input("Enter numbers separated by space: ").split()))
        multiples_of_three(arr)
    except:
        print("Invalid array input")

    seq = "[((())()(())]]"
    print(f"Bracket sequence: {seq}")
    if check_brackets(seq):
        print("The bracket sequence is correct")
    else:
        print("The bracket sequence is NOT correct")
        print("To fix it, replace the last ']' with ')'")
