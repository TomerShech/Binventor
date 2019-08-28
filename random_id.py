import random, string, time
ID = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
print(ID)