# Any one explane what is this for. I have saw this on internet.

# employed | vacation 
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false

def set_alarm(emp, vac):
    return(emp and not vac)
print("Answer following in True or False.")
emp = input("You are an employed. ").capitalize().strip()
if emp == "True": emp = True
if emp == "False": emp = False
vac = input("You are on vacation. ").capitalize().strip()
if vac == "True": vac = True
if vac == "False": vac = False
print(set_alarm(emp,vac))