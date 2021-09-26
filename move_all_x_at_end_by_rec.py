def moveAllX(s,i,c,ns):
    if i == len(s):
        for j in range(c):
            ns+="x"
        print(ns)
        return
    if s[i]=="x":
        c+=1
    else:
        ns+=s[i]
    moveAllX(s, i+1, c, ns)
inps = "xabxcxd"
moveAllX(inps,0,0,"")