# STRING JOIN =========================

a = ["MY", "NAME", "IS", "RAJ"]
b = " ".join(a)

print (b)

# String Strip =========================

word = "  Kuldip Sutreja    "

print("strip: ",len(word.strip()))
print("lstrip: ",len(word.lstrip()))
print("rstrip: ",len(word.rstrip()))

print("strip: ", word.strip())
print("lstrip: ", word.lstrip())
print("rstrip: ", word.rstrip())

print (len(word))


# Remove Non-Alphabetic Character =========================

gmail = "ksutreja07@gmail.com,!!"

clean = ""

for char in gmail:
    if char.isalpha():
        clean += char
        
print (gmail)
print (clean)


# String Cheking Method ====================

x = "Kuldip07"
print (x.isalpha())
print (x.isdigit())
print (x.islower())
print (x.isupper())
print (x.isspace())

# Reverse String ===============================

text = 'Python'

reverse_text = "".join(reversed(text))

reverse_text1 = list(text)

reverse_text1.reverse()

print("".join(reverse_text1))

print(text[::-1])

print(reverse_text)

# Plindrome
'''
text = input("\n Enter a string to check palindrome:")

reverse_text = text[::-1]

print(text)

print(reverse_text)

if text.lower() == reverse_text.lower():
  print("Plindrome")
else:
  print("Not Plingrome")
'''
# Escape Characters

print("Hello\nWorld")
print("Hello\tworld")
print("she talk \"hello\"")
print('It\'s Python')
print("C:\\Python")