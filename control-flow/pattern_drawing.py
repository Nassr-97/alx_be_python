pattern_sizen = int(input("Enter the size of the pattern:"))
i = 0

while i < pattern_sizen:
    for j in range(0, pattern_sizen):
        print("*", end="")
    print("")
    i += 1
