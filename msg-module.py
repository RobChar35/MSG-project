import random

#Java and bedrock function
def java_or_bedrock(limit, start, end):
    symbols = random.choice(" -")
    print(symbols, end="")
    for i in range(limit):
        random_number = random.randint(start, end)
        print(random_number, end="")

#Your own choice
def selection():
    limit_s = int(input("Write a limit: "))
    start_s = int(input("Write the number you want to begin: "))
    end_s = int(input("Write the number you want to end: "))
     
    if limit_s == 0:
        print("ERROR: You must define a limit greater than 0.")
    else:
        java_or_bedrock(limit_s, start_s, end_s)

#Random values in java_or_bedrock function
def get_lucky():
    limit_gl = random.randint(5, 19)
    start_gl = random.randint(0, 9)
    end_gl = random.randint(0, 9)
    java_or_bedrock(limit_gl, start_gl, end_gl)
get_lucky()