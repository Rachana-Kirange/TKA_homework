import numpy as np
arr = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])

print("Pairs whose sum is 10:")
for i in range(len(arr)):
    for j in range(i, len(arr)): 
        if i != j and arr[i] + arr[j] == 10:
            print(f"{arr[i]} + {arr[j]} = 10")
