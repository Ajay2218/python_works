

"""
Error handling

(try,except,finally) -> block
raise,assert -> keywords

1 -> syntax error
2 -> logical error
3 -> runtime error

try:
    doubtful code

expect:
    handling code

finally:
    clean up processing

raise custom error 

assert for debugging

"""

#example

n1 = int(input("enter number1 = "))
n2 = int(input("enter number2 = "))

try:

    result = n1 / n2

    print(result)
except Exception as e:
    print(e)


print("file operations")

print("database commit")

print("program finished")
