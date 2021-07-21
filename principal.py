import random

#Java function
def java_or_bedrock(limit):
    symbol = " -"
    for i in range(limit):
        print(9, end="")    
    print(random.choice(symbol), random.randint(10000, 9999999999999999999), end="")
java_or_bedrock(10)