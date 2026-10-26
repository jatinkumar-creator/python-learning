# if x > 5
#     print("big")                    # SyntaxError: missing colon

# else if x < 0:                      # SyntaxError: use elif

# if True:
# print("no indent")                  # IndentationError

# for i in range(5.0):                # TypeError: range needs integers
#     print(i)

# for i in range(0, 1, 0.1):          # TypeError
#     print(i)

# x = 0
# while x < 5:
#     x =+ 1                          # infinite loop! "=+" is not "+=". Ctrl + C to stop

#Remove the # from one block at a time, run it, read the error, and put the # back.