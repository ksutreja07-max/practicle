'''

# % formatting

print("% Formatting")

name="Kuldip"
city="Junagadh"
age = 18

print("My name is %s and my city is %s and my age is %d." % (name , city ,  age))

'''


'''

%s : String
%d : Integer
%f : Float
%.2f : Float with 2 decimal places

'''

# String Case Manipulation=====================

word = "PYTHON IS IMPORTANT"

print("Original Case :" , word)
print("Upper case :", word.upper())
print("Lower case :", word.lower())
print("Title case :", word.title())
print("Capitalize case : ",word.capitalize())
print("Swap case : ",word.swapcase())


# String Searching=============================

sentence = "Python is a programming language."

print (sentence)

print ("python position : ", sentence.find("Python"))
print ("python position : ", sentence.find("P"))
print ("python exist : ", "Python" in sentence)
print ("python index : ", sentence.index("Python"))


print(sentence.startswith("P"))
print(sentence.startswith("Python"))
print(sentence.startswith("is"))
print(sentence.endswith("."))
print(sentence.endswith("e."))
print(sentence.endswith("language"))


# String Replacement=============================

text = "i love my country. My country is India."
new_text = text.replace("country", "nation")
print ("main text : ", new_text)


# String Counting =============================

data = "date mining is very difficult."
print (data.count("i"))


# String Split ================================

ration = "soap, shampoo, oil, honey"
ration_list = ration.split(",")
print (ration_list)

data = "date mining is very difficult."
words = data.split()
print (words)

multilines = """amazon
flipkart
meesho
myntra"""

result = multilines.split("\n")
print (result)

for i in result:
    print(i)