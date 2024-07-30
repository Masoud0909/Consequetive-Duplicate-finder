# Find if user enters two same numbers consequetively

identical = bool (False)
first=input ("Enter the first number: ")
while (identical==False):
    second=input ("Enter the next number: ")
    if(first==second):
        identical=True
        print("Found Two consequetive identitcal numbers!")
    else:
        first=second

