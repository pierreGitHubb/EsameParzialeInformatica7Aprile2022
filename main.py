
clienti = 0 
portafoglio = 150
scontrino = open("scontrino", 'w')

clienti+=1

if clienti > 0 and  clienti < 10 :
    for x in range(clienti):
        clienti -= 1
        print("Lei può entrare nel supermarcato")

        print("Le mostro il nostro catalogo:")
        catalogo = {"Cibo":"Patatine, Verdure, Carne di maiale e Colazione", "Bevande":"Acqua, Coca-Cola, Sprite, Fanta", "Alcolici":"Vino"}
        print(catalogo)
        scelta = input("Che cosa desidera comprare?: ")
        scelta2 = input("Cosa desidera nello specifico?: ")

        if scelta == "Cibo":
            if scelta2 == "Patatine":
                print("Patatine, prezzo addebbitato: 0.50")
                portafoglio-=0.50
                print("Lei ha pagato 0.50 centesimi")
                print("Adesso ha: " + str(portafoglio) + " euro")

            if scelta2 == "Verdure":
                print("Verdure, prezzo: 5.0")
                portafoglio-=5.0
                print("Lei ha pagato 5.0 euro")
                print("Adesso ha: " + str(portafoglio) + " euro")

            if scelta2 == "Carne di maiale":
                print("Carne di maiale all'etto, prezzo: 2.50")
                portafoglio-=2.50
                print("Lei ha pagato 2.50 euro")
                print("Adesso ha: " + str(portafoglio) + " euro")

            if scelta2 == "Colazione":
                scelta3 = input("Colazione, prodotti: Cereali, Barrette di Cioccolato: ")
                if scelta3 == "Cereali":
                    print("Cereali, prezzo addebbitato: 3.50")
                    portafoglio-=3.50
                    print("Lei ha pagato 3.50 euro")
                    print("Adesso ha: " + str(portafoglio) + " euro")
                    scontrino.write(scelta3+" \n")
                
                if scelta3 == "Barrette di Cioccolato":
                    print("Barrette di Cioccolato, prezzo addebbitato: 6.50")
                    portafoglio-=6.50
                    print("Lei ha pagato 6.50 euro")
                    print("Adesso ha: " + str(portafoglio) + " euro")
                    scontrino.write(scelta3+" \n")
        
        if scelta == "Bevande":
            if scelta2 == "Acqua":
                print("Acqua, prezzo: 0.40")
                portafoglio-=0.40
                print("Lei ha pagato 0.40 centesimi")
                print("Adesso ha: " + str(portafoglio) + " euro")

            if scelta2 == "Coca-Cola":
                print("Coca-Cola, prezzo: 1.50")
                portafoglio-=1.50
                print("Lei ha pagato 1.5 euro")
                print("Adesso ha: " + str(portafoglio) + " euro")

            if scelta2 == "Sprite":
                print("Sprite, prezzo: 1.0")
                portafoglio-=1.0
                print("Lei ha pagato 1.0 euro")
                print("Adesso ha: " + str(portafoglio) + " euro")

            if scelta2 == "Fanta":
                print("Fanta prezzo: 2.50")
                portafoglio-=2.50
                print("Lei ha pagato 2.50 euro")
                print("Adesso ha: " + str(portafoglio) + " euro")

        if scelta == "Alcolici":
            if scelta2 == "Vino":
                scelta6 = input("Lo vuole rosso, bianco, rosato; scelga: ")
                if scelta6 == "Rosso":
                    print("Vino rosso, prezzo: 15.60")
                    portafoglio-=15.60
                    print("Lei ha pagato 15.60")
                    print("Adesso ha: " + str(portafoglio) + " euro")
                    scontrino.write(scelta6+" \n")

                if scelta6 == "Bianco":
                    print("Vino bianco prezzo: 12.0")
                    portafoglio-=12.0
                    print("Lei ha pagato 12.0 euro")
                    print("Adesso ha: " + str(portafoglio) + " euro")
                    scontrino.write(scelta6+" \n")

                if scelta6 == "Rosato":
                    print("Vino rosato per dolce, prezzo: 24.99")
                    portafoglio-=24.99
                    print("Lei ha pagato 24.99 euro")
                    print("Adesso ha: " + str(portafoglio) + " euro")
                    scontrino.write(scelta6+" \n")
            


        scontrino.write(scelta+" \n")
        scontrino.write(scelta2+" \n")


        
if clienti > 10:
    print("Mi dispiace ma non può entrare nel supermercato")