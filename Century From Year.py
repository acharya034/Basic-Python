year = 100 # let or take input
year = int(input("Enter the year."))
if year % 100 == 0: 
    century = year//100
else:
    century = year//100 +1

if century == 1:
    cent = str(century) + "st"
elif century == 2:
    cent = str(century) + "nd"
elif century == 3:
    cent = str(century) + "rd"
else:
    cent = str(century) + "th"

print("it's ",cent ," century.")
