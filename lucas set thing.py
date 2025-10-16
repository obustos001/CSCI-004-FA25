omar = [2, 1]

omar.append(omar[1] + omar[0])  

for n in range(2,5):
    omar[n] = omar[n - 1] + omar[n - 2]


print("omar is ", omar)