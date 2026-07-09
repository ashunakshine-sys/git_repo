
def duplicate():
    str1= input("Enter first string")
    str2=input("enter second string")
    s1=set(str1) # split string and remove duplicates
    s2=set(str2)
    print(s1)
    print(s2)
    str3=s1 & s2 # gives only duplicate letter
    print(str3)

duplicate()