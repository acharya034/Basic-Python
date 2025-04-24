print("🎆🎆Number systerm🎆🎆")
noq = 0
while True:
    if noq == 0:
        c = input("""Choose any one:-
        1.Binary to decimal 
        2.Decimal to binary
        3.Octal to decimal
        4.Decimal to octal
        5.Octal to binary
        6.Binary to octal
        7.Hexdecimal to decimal
        8.Decimal to hexdecimal
        9.Hexdecimal to binary
        10.Binary to hexdecimal
        Other To Exit
        >>>""")
        noq = int(input("How many question are there:-"))
    else :
        print("next")
    if c == '1':
        val1 = ""
        val2 = ""
        val3 = ""
        b = '10'
        count = 0
        n = input("enter binary number\n")
        l = list(n)
        a = []
        for i in n:
            if i not in b:
                count = 1
                if i not in a:
                    a.append(i)
                pass
            else:
                pass
        sum = 0
        l.reverse()
        if count:
            if len(a) == 1:
                print(a," is not binary number. 😢")
            else:
                print(a," are not binary numbers. 😢")
        else:
            for i in range(len(l)):

                val1 += (f"{int(l[i])}x2^{i} + ")
                q = 2**i
                val2 += (f"{int(l[i])}x{q} + ")
                r = int(l[i])*q
                val3 += (f"{r} + ")
                sum = sum+int(l[i])*2**i
            print(val1[:-2])
            print()
            print(val2[:-2])
            print()
            print(val3[:-2])
            print()
            print(sum)
            print()
            print("(",n,")2 = (",sum,")10 🎁ANS🎁")
            noq -= 1
    elif c == '2':
        n = input("enter decimal number\n")
        l=list()
        d = '0123456789'
        count = 0
        a = []
        for i in n:
            if i not in d:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not decimal number. 😢")
            else:
                print(a," are not decimal numbers. 😢")
        else:
            n = int(n)
            while n!=0:
                r = n%2
                l.append(r)
                if n == 1:
                    print("    1")
                else:
                    print(f"2 | {n} | {r}")
                n=n//2
            l.reverse()
            for i in l:
                print(i,end="")
            print("   🎁ANS🎁")
            noq -= 1
    elif c == '3':
        o = '01234567'
        sum=0
        val1 = ""
        val2 = ""
        val3 = ""
        count = 0
        n = input("enter octal number\n")
        l = list(n)
        3
        l.reverse()
        count = 0
        a = []
        for i in n:
            if i not in o:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not octal number. 😢")
            else:
                print(a," are not octal numbers. 😢")
        else:
            for i in range(len(l)):
                val1 += (f"{int(l[i])}x8^{i} + ")
                q = 8**i
                val2 += (f"{int(l[i])}x{q} + ")
                r = int(l[i])*q
                val3 += (f"{r} + ")
                sum=(sum+r)
            print(val1[:-2])
            print()
            print(val2[:-2])
            print()
            print(val3[:-2])
            print()
            print(sum," 🎁ANS🎁")
            noq -= 1
    elif c == '4':
        n=input("enter decimal number\n")
        l=list()
        b = '0123456789'
        count = 0
        a = []
        for i in n:
            if i not in b:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not decimal number. 😢")
            else:
                print(a," are not decimal numbers. 😢")
        else:
            n=int(n)
            while n!=0:
                r = n%8
                l.append(r)
                if n < 8:
                    print("   ",n)
                else:
                    print(f"8 | {n} | {r}")
                n=n//8
            l.reverse()
            for i in l:
                print(i,end="")
            print("   🎁ANS🎁")
            noq -= 1
    elif c == '5':
        l=list()
        o = '01234567'
        count = 0
        n = input("enter octal number\n")
        a = []
        for i in n:
            if i not in o:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not octal number. 😢")
            else:
                print(a," are not octal numbers. 😢")
        else:
            l = []
            for j in range(len(n)):
                h = n[j]
                if h == '0':
                    binum = '000'
                elif h == '1':
                    binum = '001'
                elif h == '2':
                    binum = '010'
                elif h == '3':
                    binum = '011'
                elif h == '4':
                    binum = '100'
                elif h == '5':
                    binum = '101'
                elif h == '6':
                    binum = '110'
                elif h == '7':
                    binum = '111'
                print(h," = ", binum)
                l.append(binum)
            binary_str = ''.join(l)
            print(binary_str + "   🎁ANS🎁")
            noq -= 1
    elif c == '6':
        b = '10'
        count = 0
        num = input("enter binary number\n")
        l = list(num)
        a = []
        for i in num:
            if i not in b:
                count = 1
                a.append(i)
                pass
            else:
                pass
        sum = 0
        l.reverse()
        if count:
            if len(a) == 1:
                print(a," is not binary number. 😢")
            else:
                print(a," are not binary numbers. 😢")
        else:
            m = -3
            n = 0
            l = []
            b = len(num) % 3
            if b == 2:
                print(num," Add (0) for balance it.")
                num = "0"+num
            elif b == 1:
                print(num," Add (00) for balance it.")
                num = "00"+num
            elif b == 0:
                num = num+""
            a = len(num) // 3
            for j in range(a):
                m = m + 3
                n = n + 3
                h = num[m:n]
                if h == '000':
                    onum = '0'
                elif h == '001':
                    onum = '1'
                elif h == '010':
                    onum = '2'
                elif h == '011':
                    onum = '3'
                elif h == '100':
                    onum = '4'
                elif h == '101':
                    onum = '5'
                elif h == '110':
                    onum = '6'
                elif h == '111':
                    onum = '7'
                l.append(onum)
                print(h," = ",onum)
            octal_str = ''.join(l)
            print(octal_str + "   🎁ANS🎁")
            noq -= 1
    elif c == '7':
        h = '0123456789ABCDEF'
        val1 = ""
        val2 = ""
        val3 = ""
        sum=0
        n = input("enter Hexdecimal number\n").upper()
        l = list(n)
        l.reverse()
        a = []
        count=0
        for i in n:
            if i not in h:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not Hexdecimal number. 😢")
            else:
                print(a," are not Hexdecimal numbers. 😢")
        else:
            for i in range(len(l)):
                if l[i] == 'A':
                    yy = 10
                elif l[i] == 'B':
                    yy = 11
                elif l[i] == 'C':
                    yy = 12
                elif l[i] == 'D':
                    yy = 13
                elif l[i] == 'E':
                    yy = 14
                elif l[i] == 'F':
                    yy = 15
                else:
                    yy = int(l[i])
                val1 += (f"{yy}x16^{i} + ")
                q = 16**i
                val2 += (f"{yy}x{q} + ")
                r = yy*q
                val3 += (f"{r} + ")
                sum=(sum+r)
            print(val1[:-2])
            print()
            print(val2[:-2])
            print()
            print(val3[:-2])
            print()
            print(sum," 🎁ANS🎁")
            noq -= 1
    elif c == '8':
        n=input("enter decimal number\n")
        l=list()
        b = '0123456789'
        count = 0
        a = []
        for i in n:
            if i not in b:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not decimal number. 😢")
            else:
                print(a," are not decimal numbers. 😢")
        else:
            re = 0
            n=int(n)
            while n!=0:
                r = n%16
                if r == 10:
                    re = '10 = A'
                    r = 'A'
                elif r == 11:
                    re = '11 = B'
                    r = 'B'
                elif r == 12:
                    re = '12 = C'
                    r = 'C'
                elif r == 13:
                    re = '13 = D'
                    r = 'D'
                elif r == 14:
                    re = '14 = E'
                    r = 'E'
                elif r == 15:
                    re = '15 = F'
                    r = 'F'
                else:
                    re = r
                l.append(r)
                if n < 16:
                    if r == 10:
                        r = 'A'
                    elif r == 11:
                        r = 'B'
                    elif r == 12:
                        r = 'C'
                    elif r == 13:
                        r = 'D'
                    elif r == 14:
                        r = 'E'
                    elif r == 15:
                        r = 'F'
                    else:
                        r = n
                    print("   ",r)
                else:
                    print(f"16 | {n} | {re}")
                n=n//16
            l.reverse()
            for i in l:
                print(i,end="")
            print("   🎁ANS🎁")
            noq -= 1
    elif c == '9':
        l=list()
        o = '0123456789ABCDEF'
        count = 0
        n = input("enter Hexdecimal number\n").upper()
        a = []
        for i in n:
            if i not in o:
                count = 1
                a.append(i)
                pass
            else:
                pass
        if count:
            if len(a) == 1:
                print(a," is not Hexdecimal number. 😢")
            else:
                print(a," are not Hexdecimal numbers. 😢")
        else:
            l = []
            for j in range(len(n)):
                h = n[j]
                if h == '0':
                    binum = '0000'
                elif h == '1':
                    binum = '0001'
                elif h == '2':
                    binum = '0010'
                elif h == '3':
                    binum = '0011'
                elif h == '4':
                    binum = '0100'
                elif h == '5':
                    binum = '0101'
                elif h == '6':
                    binum = '0110'
                elif h == '7':
                    binum = '0111'
                elif h == '8':
                    binum = '1000'
                elif h == '9':
                    binum = '1001'
                elif h == 'A':
                    binum = '1010'
                elif h == 'B':
                    binum = '1011'
                elif h == 'C':
                    binum = '1100'
                elif h == 'D':
                    binum = '1101'
                elif h == 'E':
                    binum = '1110'
                elif h == 'F':
                    binum = '1111'
                print(h," = ", binum)
                l.append(binum)
            binary_str = ''.join(l)
            print(binary_str + "   🎁ANS🎁")
            noq -= 1
    elif c == '10':
        b = '10'
        count = 0
        num = input("enter binary number\n")
        l = list(num)
        a = []
        for i in num:
            if i not in b:
                count = 1
                a.append(i)
                pass
            else:
                pass
        sum = 0
        l.reverse()
        if count:
            if len(a) == 1:
                print(a," is not binary number. 😢")
            else:
                print(a," are not binary numbers. 😢")
        else:
            m = -4
            n = 0
            l = []
            b = len(num) % 4
            if b == 3:
                print(" Add (0) for balance it.")
                num = "0"+num
            elif b == 2:
                print(" Add (00) for balance it.")
                num = "00"+num
            elif b == 1:
                print(" Add (0) for balance it.")
                num = "0"+num
            print(num)
            a = len(num) // 4
            for j in range(a):
                m = m + 4
                n = n + 4
                h = num[m:n]
                if h == '0000':
                    onum = '0'
                elif h == '0001':
                    onum = '1'
                elif h == '0010':
                    onum = '2'
                elif h == '0011':
                    onum = '3'
                elif h == '0100':
                    onum = '4'
                elif h == '0101':
                    onum = '5'
                elif h == '0110':
                    onum = '6'
                elif h == '0111':
                    onum = '7'
                elif h == '1000':
                    onum = '8'
                elif h == '1001':
                    onum = '9'
                elif h == '1010':
                    onum = 'A'
                elif h == '1011':
                    onum = 'B'
                elif h == '1100':
                    onum = 'C'
                elif h == '1101':
                    onum = 'D'
                elif h == '1110':
                    onum = 'E'
                elif h == '1111':
                    onum = 'F'
                l.append(onum)
                print(h," = ",onum)
            octal_str = ''.join(l)
            print(octal_str + "   🎁ANS🎁")
            noq -= 1
    else :
        print("Thanks for given your time😀")
        break