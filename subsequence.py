def printsubsequence(s,i,res):
    if i==len(s):
        print(res)
        return
    printsubsequence(s,i+1,res+s[i])
    printsubsequence(s,i+1,res)
s=input()
print("subsequences :")
printsubsequence(s,0,'')