from itertools import permutations as P
 
def splitExpression(expression, sep):
    numbers =[]
    operations = []
    integer =""
    for s in expression:
        if s in sep:
            numbers.append(int(integer))
            operations.append(s)
            integer = ""
        else:
            integer += s
    numbers.append(int(integer))
 
    return numbers, operations
 
def solution(expression):
    
    sep = ['*', '+', '-']
    numbers, operations = splitExpression(expression, sep)
 
    answer = 0
    for priority_ops in list(P(sep, 3)):
        temp_num = numbers[:]
        temp_op =  operations[:]
 
        for op in priority_ops:
            while True:
                try:
                    opIndex = temp_op.index(op)
                    temp_op.pop(opIndex)
                    left = temp_num.pop(opIndex)
                    right = temp_num.pop(opIndex)
 
                    if op == "+":
                        temp_num.insert(opIndex, left + right)
                    elif op == "-":
                        temp_num.insert(opIndex, left - right)
                    else:
                        temp_num.insert(opIndex, left * right)
                except:
                    break
 
        result = abs(temp_num[0])
        if result > answer:
            answer = result
    return answer