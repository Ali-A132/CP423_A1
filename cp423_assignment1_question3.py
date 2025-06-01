# Question 3: Query Support and System Evaluation [30 points]
# Support and evaluate queries such as:
# • x OR y
# • x AND y
# • x AND NOT y
# • x OR NOT y
# Develop generalized code capable of handling queries with multiple terms and logical operators (AND, OR, NOT).

from cp423_assignment1_question2 import InvertedIndex

def evaluateQuery(post, docIdList):
    stack = []

    for token in post:
        if token == 'NOT':
            operand = stack.pop()
            stack.append(docIdList - operand)
        elif token == 'AND':
            right = stack.pop()
            left = stack.pop()
            stack.append(left & right)
        elif token == 'OR':
            right = stack.pop()
            left = stack.pop()
            stack.append(left | right)
        else:
            stack.append()

    return stack

queries = [
    "ontario OR quebec",
    "ontario AND quebec",
    "ontario AND NOT quebec",
    "ontario OR NOT quebec",
]