import random
def pass_gen(length=12):
    l=["@","#","$","&","%","^","*","(",")","+","="]
    upper = chr(random.randint(65,90))
    lower = chr(random.randint(97,122))
    special = random.choice(l)
    num = random.randint(100000,999999)
    password = upper + lower + special + str(num) + upper + lower + special
    return password

result = pass_gen(12)
print(result)