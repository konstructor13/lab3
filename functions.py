
def fibonachi(n):
    numberList = ([0, 1])
    if (n == 0):
        return [0]
    for i in range(2, n):
        numberList.append(numberList[i - 2] + numberList[i - 1])
    return numberList

def bubble_sort(inputList):
    for i in range(len(inputList) - 1):
        for j in range(len(inputList) - 1):
            if (inputList[j] > inputList[j + 1]):
                temp = inputList[j]
                inputList[j] = inputList[j + 1]
                inputList[j + 1] = temp
    return inputList

def calculator(a, b, z):
    if (z == "+"):
        return a+b
    elif (z == "-"):
        return a-b
    elif (z == "*"):
        return a*b
    elif (z == "/"):
        return a/b