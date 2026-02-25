class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i.isalpha()==True or i.isdigit()==True:
                a=a+i.lower()
        b=a[::-1]
        print (a)
        print(b)
        if a==b:
            return True
        return False