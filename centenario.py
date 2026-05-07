import datetime  # Importiamo la libreria per gestire le date

# Otteniamo l'anno corrente in automatico
anno_attuale = datetime.datetime.now().year

nome = input("Come ti chiami? ")
eta = int(input("Quanti anni hai? "))

anni_al_centenario = 100 - eta
anno_del_centenario = anno_attuale + anni_al_centenario

print(f"Ehi {nome}, compirai 100 anni nel {anno_del_centenario}!")