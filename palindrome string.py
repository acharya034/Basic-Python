# True if the text is same as its reverse version.

text = input("enter a text ")
rtext = ""
text = text.strip().lower()

rtext = ''.join(reversed(text))
print(rtext) 

if text == rtext:
    print("Yes it's a palindrome string.")
else:
    print("no try again!")