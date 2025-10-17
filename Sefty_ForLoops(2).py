# Print numbers from 1 to 5

for i in range (1,6):
    print((f"Count:{i}"),end=", ")

    
for i in range (1,6):
    if i < 5:
        print((f"Count: {i},",),end=" ")
    else:
        print(f"Count: {i}")