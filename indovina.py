import random

# Il computer sceglie un numero tra 1 e 10
numero_segreto = random.randint(1, 10)
tentativo = 0

print("Ho pensato a un numero tra 1 e 10. Prova a indovinarlo!")

# Il ciclo continua finché il tentativo è diverso dal numero segreto
while tentativo != numero_segreto:
    tentativo = int(input("Inserisci il tuo numero: "))

    if tentativo < numero_segreto:
        print("Troppo basso! Riprova.")
    elif tentativo > numero_segreto:
        print("Troppo alto! Riprova.")
    else:
        print("GRANDE! Hai indovinato!")