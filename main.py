#! /usr/bin/python3

from time import sleep

NORMAL_PRECEDENCE = 0
HIGH_PRECEDENCE = 1
HIGHEST_PRECEDENCE = 2

precedence = {
    "+": NORMAL_PRECEDENCE,
    "-": NORMAL_PRECEDENCE,
    "*": HIGH_PRECEDENCE,
    "/": HIGH_PRECEDENCE,
    "^": HIGHEST_PRECEDENCE
}


def infix_to_rpn(string):
    output = []
    stack = []
    # keeps track of long digits like anything >= 10
    num = ''
    for token in s:
        if token is ' ':
            continue
        if token.isdigit():
            num += token
            # output.append(token)
        else:
            # once done add the last digit. If there is one.
            if len(num) > 0:
                output.append(num)
                num = ''

        if is_operator(token):
            while len(stack) > 0 and is_operator(peek_stack(stack)):
                if precedence[token] <= precedence[peek_stack(stack)]:
                    output.append(stack.pop())
                break
            stack.append(token)
        if token is "(":
            stack.append(token)
        if token is ")":
            while len(stack) > 0 and peek_stack(stack) is not "(":
                output.append(stack.pop())
            stack.pop()
    else:
        # once done add the last digit. If there is one.
        if len(num) > 0:
            output.append(num)

    while len(stack) > 0:
        output.append(stack.pop())
    return output


def calculate_rpn(queue):
    stack = []
    for token in queue:
        if token.isdigit():
            stack.append(token)
        if is_operator(token):
            x = float(stack.pop())
            y = float(stack.pop())
            # y comes first (i.e y / x not x / y)
            result = calculate(y, x, token)
            # print(x, y, token, result)
            stack.append(result)
    return stack.pop()


def is_operator(token):
    return token is "+" or token is "-" or token is "*" or token is "/" or token is "^"


def peek_stack(stack):
    return stack[-1]


def calculate(x, y, token):
    result = x + y if token is "+" else x - \
        y if token is "-" else x * y if token is "*" else x / y if token is "/" else x**y
    return result


print("Enter the expression you want evaluated:", end=" ")
s = input()
rpn_queue = infix_to_rpn(s)
print(rpn_queue)
result = calculate_rpn(rpn_queue)
print(result)
