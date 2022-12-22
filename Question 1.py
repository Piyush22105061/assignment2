# Defining a "input" variable 
input = "Python is a case sensitive language"

# part(a)- finding the length of given string.
print("Length of the input string is",len(input))

# part(b)- reversing the order of the input string in one line code.
Reverse_order = input[35::-1]
print( "the reverse order is'", Reverse_order ,"'")

# part(c)- using slice function storing "a case sensitive" in a new string.
phrase = input[10:27]
print('''the sliced string is "''', phrase,'''"''')

# part(d)- replacing "a case sensitive" with "object oriented".
New_input = input.replace("a case sensitive","object oriented")
print('''Updated string is "''',New_input,'''"''')

# part(e)- finding index of substring "a" in the input string
index_of_a = input.find("a") 
print("The index of 'a' is",index_of_a)

# part(f)- removing the white spaces from the input string.
updated_input = input.replace(" ","")
print("The new string is '",updated_input,"'")


