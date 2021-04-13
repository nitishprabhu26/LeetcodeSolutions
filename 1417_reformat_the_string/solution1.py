class Solution:
    def reformat(self, s: str) -> str:
        list1=[]
        list2=[]
        result=""
        str1="abcdefghijklmnopqrstuvwxyz"
        str2="0123456789"        
        set1=set(str1)
        set2=set(str2)
        for i in s:
            if i in set1:
                list1.append(i)
            elif i in set2:
                list2.append(i)
                
        len1=len(list1)
        len2=len(list2)
        diff=abs(len1-len2)
        if diff==1 or diff==0:
            if len1>=len2:
                while(list1 and list2):
                    result+=list1.pop()+list2.pop()
                while(list1):
                    result+=list1.pop()
                
            else:
                while(list1 and list2):
                    result+=list2.pop()+list1.pop()
                while(list2):
                    result+=list2.pop()
            return result
        else:
            return ""

num1 = "qpwn55656"
obj = Solution()
print(obj.reformat(num1))