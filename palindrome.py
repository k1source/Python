def palindrome(x):
    number = x
    while(x>0):
        rev = 0
        x = x%10
        rev = rev*10+x
    if(number==rev):
        print("true")
    else:
        print("false")

palindrome(121)
palindrome(134)
