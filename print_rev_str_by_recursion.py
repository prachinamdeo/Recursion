def printRev(s,i):
	if i == 0:
		print(s[i])
		return
	print(s[i],end="")
	printRev(s,i-1)
s=input()
printRev(s,len(s)-1)