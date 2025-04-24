text = input("enter a word -->")
rtext = ""
j = len(text)
for i in range(j):
    rtext =text[i] + rtext

print(rtext)