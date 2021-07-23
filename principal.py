import random

#Java and bedrock function
def java_or_bedrock(limit, start, end):
    symbols = random.choice(" -")
    print(symbols, end="")
    for i in range(limit):
        random_number = random.randint(start, end)
        print(random_number, end="")

#Simple menu