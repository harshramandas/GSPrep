def TOH(n,x,y,z):
    global i
    if n >= 1:
        TOH(n-1,x,z,y)
        i+=1
        print("{}: Move top-most disc from ".format(i)+x+" to "+y)
        TOH(n-1,z,y,x)
n = int(input("Enter no. of discs: "))
print("The steps are:\n")
i = 0
TOH(n, "Source", "Destination", "Auxilliary")
print("\nNo. of steps = {}".format(i))
print("Time complexity is 2^n")
print("Recursion is used to move lowermost disc.")