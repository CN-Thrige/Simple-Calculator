# alle side (s.) i denne opgave er fra Starting out with Python 5th ed.

# s. 171-172 om The while Loop: A Condition-Controlled Loop
keep_going = 'j'
while keep_going == 'j':
    valg = float(input("vælg mellem\n"
                   "1. plus:\n" 
                   "2. Minus:\n"
                   "3. Gange:\n" 
                   "4. Normal division:\n" 
                   "5. Floor division:\n" 
                   "6. Modulus:\n"
                   "svar:\t"))
    # Jeg har brugt kilde escape character \n og \t (s. 69).

 #float(), bruges over int(), fordi at float kan bruges med decimal el. kommatal (s. 51-53)
    NUM1 = float(input("Skriv det første tal:\t"))
    NUM2 = float(input("Skriv det andet tal:\t"))

# I det næste afsnit gøres der brug af decision structure (s. 120-124)
    # Samtidig bruges der relational operatoren, equal to.
        # equal to == bestemmer om "operatoren" er den samme på enten venstre eller højre side.
            # #Hvis værdi er den samme på hver side, så er udtrykket (expression) korrekt (s.  124).

#nedenunder gøres der brug af en single alternative decision structure (s. 120).
    #Hvis man vælger at fx skrive 1 ovenover, så går Python Interpreteren igennem dem for at teste dem om de er sande.
    #Siden jeg har programmeret den til at være equal to, så ved python at valget af 1, er = med NUM1 + NUM2, osv. (s. 121)

    if valg == 1:
        print("=\t", NUM1 + NUM2)

    if valg == 2:
        print("=\t", NUM1 - NUM2)

    if valg == 3:
        print("=\t", NUM1 * NUM2)

    if valg == 4:
        print("=\t", NUM1 / NUM2)

    if valg == 5:
        print("=\t", NUM1 // NUM2)

    if valg == 6:
        print("=\t", NUM1 % NUM2)

    keep_going = input('Udregn mere:' + '(tryk Enter j for ja eller n for nej):\t')
    #s. 171-172 om The while Loop: A Condition-Controlled Loop


