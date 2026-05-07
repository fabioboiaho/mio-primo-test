# Chiediamo le informazioni all'utente
nome = input("Come ti chiami? ")
eta = input("Quanti anni hai? ")

# Trasformiamo l'età in un numero (per poter fare i calcoli)
eta_numerica = int(eta)
anni_mancanti = 100 - eta_numerica

# Stampiamo il risultato
print(f"Ciao {nome}! Ti mancano {anni_mancanti} anni per arrivare a 100!")
