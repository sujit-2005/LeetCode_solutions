class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i=0
        j=0
        n1=len(version1)
        n2=len(version2)
        while i<n1 or j<n2:
            revision1="0"
            revision2="0"
            while i<n1 and version1[i]!=".":
                revision1+=version1[i]
                i+=1
            while j<n2 and version2[j]!=".":
                revision2+=version2[j]
                j+=1
            if int(revision1)<int(revision2):
                return -1
            elif int(revision1)>int(revision2):
                return 1
            i+=1
            j+=1
        return 0
