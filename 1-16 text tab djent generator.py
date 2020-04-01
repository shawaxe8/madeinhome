#1/16 text tab djent generator 
import random
djent = ["0", "x", "-"]

print("|",end="")
for i in range(16):
    print(random.choice(djent),end="")
print("|")