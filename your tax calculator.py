print("Calculate your tax only you need to enter your yearly salary.")
def again():
    print("Something is wrong!,try again")
    cal()
def cal():
    state = input("Are you a single.(y/n) ")
    if state.lower().strip() == 'y':
        # Tax for single
        t1 = 500000 # 5,00,000
        t2 = 700000 # 7,00,000
        t3 = 1000000 # 10,00,000
        t4 = 2000000 # 20,00,000
        t5 = 5000000 # 50,00,000

        #Tax percentage!
        p1 = 1 / 100
        p2 = 10 / 100
        p3 = 20 / 100
        p4 = 30 / 100
        p5 = 36 / 100
        p6 = 39 / 100
    elif state.lower().strip() == 'n':
        # Tax brackets for couples
        t1 = 700000  # 7,00,000
        t2 = 1000000  # 10,00,000
        t3 = 1400000  # 14,00,000
        t4 = 2500000  # 25,00,000
        t5 = 6000000  # 60,00,000

        # Tax percentages
        p1 = 1 / 100
        p2 = 10 / 100
        p3 = 20 / 100
        p4 = 30 / 100
        p5 = 36 / 100
        p6 = 39 / 100

    else:
        again()


    salary = int(input("Enter your income\n \t -->"))
    if salary > 0:
        if salary <= t1 :
            tax = p1*salary
        elif salary <= t2 :
            tax = p1*t1
            tax += p2*(salary-t1)
        elif salary <= t3 :
            tax = p1*t1
            tax += p2*(t2-t1)
            tax += p3*(salary-(t2))
        elif salary <= t4 :
            tax = p1*t1
            tax += p2*(t2-t1)
            tax += p3*(t3-t2)
            tax += p4*(salary-(t3))
        elif salary <= t5 :
            tax = p1*t1
            tax += p2*(t2-t1)
            tax += p3*(t3-t2)
            tax += p4*(t4-t3)
            tax += p5*(salary-(t4))
        elif salary >= t5 :
            tax = p1*t1
            tax += p2*(t2-t1)
            tax += p3*(t3-t2)
            tax += p4*(t4-t3)
            tax += p5*(t5-t4)
            tax += p6*(salary-(t5))

        else:
            again()
    else:
        again()




    print("You have to pay ",tax," for your salary ",salary,", pay your tax on time.")
cal()
