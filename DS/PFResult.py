S = input("Enter expression: ")
L = []
for s in S:
	if s == '+' or s == '-' or s == '*' or s == '/':
		a = L.pop()
		b = L.pop()
		L.append('('+b+s+a+')')
	else:
		L.append(s)
print(L[0])