

keep_going = 'j'
while keep_going == 'j':
    valg = float(input("vælg mellem\n"
                   "1. plus:\n" 
                   "2. Minus:\n"
                   "3. Gange:\n" 
                   "4. Normal division:\n" 
                   "5. Floor division:\n" 
                   "6. Modulus:\n"
                       "7. Radius, areal og omkreds"
                   "Enter:\t"))

    n1 = float(input("Første tal:\t"))
    n2 = float(input("Andet tal:\t"))

    if valg == 1:
        print(n1, '+', n2, '=', n1 +  n2)

    elif valg == 2:
        print(n1, '-', n2, '=', n1 - n2)

    elif valg == 3:
        print(n1, '*', n2, '=', n1 * n2)

    elif valg == 4:
        print(n1, '/', n2, '=', n1 / n2)

    elif valg == 5:
        print(n1, '//', n2, '=', n1 // n2)

    elif valg == 6:
        print(n1, '%', n2, '=', n1 % n2)

    elif valg == 7:
        pi = 3.14
        # definerer pi
        # n1= radius
        print(pi * n1 ** 2)

        print("Radius:", n1, "cm")
        # udregning af Radius

        print("Areal:", pi * n1 ** 2, "cm")
        # udregning af areal

        print("Omkreds:", 2 * pi * n1, "cm")
        # udregning af omkreds


    keep_going = input('Udregn mere:' + '(tryk Enter j for ja eller n for nej):\t')
