S = input("Enter expression: ")
L = []
O = ""
d = { '-' : 1, '+' : 2, '*' : 3, '/' : 4, '(' : 0}
for s in S:
	if s == '+' or s == '-' or s == '*' or s == '/' or s == '(':
		if not L:
			L.append(s);
		elif d[L[-1]] < d[s]:
			L.append(s)
		else:
			while L:
				O += L.pop()
	elif s == ')':
		while L[-1] != '(':
			O += L.pop()
		L.pop()
	else:
		O += s
while L:
	O += L.pop()
print("Output = " + O)
