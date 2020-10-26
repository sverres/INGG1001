# sam.py - anayser av samordna opptak

with open("poenggrenser_2011.csv") as f:

    studier = f.readlines()

def antall_studier_alle(studier):

    studier_alle = []

    for studie in studier:
        poenggrense = studie.split(",")
        if poenggrense[1][1] == "A":
            studier_alle.append(poenggrense[0])
    
    print("Antall studier der alle kom inn:", len(studier_alle))

def snitt_NTNU(studier):

    studier_NTNU = []

    for studie in studier:
        poenggrense = studie.split(",")
        if poenggrense[0][1:5] == "NTNU" and poenggrense[1][1] != "A":
            studier_NTNU.append(float(poenggrense[1]))
    
    print("Gjennomsnitt for NTNU:", round(sum(studier_NTNU)/len(studier_NTNU), 2))

antall_studier_alle(studier)
print("Antall studier totalt:", len(studier))
snitt_NTNU(studier)
