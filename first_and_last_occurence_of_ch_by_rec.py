def firstLastOccurence(s,c,i,first,last):
	if i == len(s):
		print("first",first)
		print("last",last) 
		return
	if s[i]==c:
		if first == None:
			first = i
		else:
			last = i
	firstLastOccurence(gs,c,i+1,first,last)
	 
gs="abaabbcdae"
firstLastOccurence(gs,"a",0,None,None)