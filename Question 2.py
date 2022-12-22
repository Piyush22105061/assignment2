# introducing "intro" variable.
intro = '''Hey, ABC here!
My SID is 22XXXXXX
I am from XYZ department and my CGPA is 9.9'''

# storing the name, SID, department, CGPA in different variables.
name = input("Enter your name\n")
SID = input("enter your SID here\n")
department = input("enter your department here\n")
CGPA = input("enter your CGPA here\n")

# Replacing the "ABC","22XXXXXX","XYZ" with a real name, SID, department
intro = intro.replace("ABC",name)
intro = intro.replace("22XXXXXX",SID)
intro = intro.replace("XYZ",department)
intro = intro.replace("9.9",CGPA)

# printing my new intro 
print(intro)