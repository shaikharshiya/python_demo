input_str=input("Eneter any String:  ")
vowels=['a','A','e','E','I','i','o','O','u','U']
str=""
for i in range(len(input_str)):
    if(input_str[i].isalpha()):
        if(input_str[i] in vowels):
            str+=input_str[i].upper()
        else:
            if(input_str[i]=='Z' ):
                str+='A'
            if(input_str[i]=='z'):
                 str+='a'
            else:
                str+=chr(ord(input_str[i])+1)
    elif(input_str[i].isdigit()):
            str+=input_str[i]
    else:
        str+=" "
print("Original String: ",input_str)
print("Encrypted String: ",str)