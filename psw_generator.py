# importazione moduli random & csv
import random
import csv

def pswGenerator():

    chars = 'ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz1234567890!"£$%&/()=?ì^*éè+ù§°à#@ò-_:.,;…–•<>'
    
    print("PASSWORD GENERATOR.")
    
    # creazione input per numero password da generare
    numero_psw = input("Quante password vuoi generare?")
    numero_psw = int(numero_psw)
    
    # creazione input per lunghezza password
    lunghezza_psw = input("Che lunghezza devono avere le password?")
    lunghezza_psw = int(lunghezza_psw)
    
    # creazione e scrittura file csv dove verranno memorizzate le password generate
    with open("/Users/user_name/Desktop/directory_name/elenco_psw.csv", "w", newline = "", encoding='utf-8') as elenco_psw:
    
        # creazione oggetto per scrivere nel file elenco_psw.csv
        writer = csv.writer(elenco_psw)
    
        # intestazione
        writer.writerow(['PASSWORD GENERATE'])
    
        # iterazione input per la creazione del numero di password
        for i in range(numero_psw):
    
            # list comprehension per creazione randomica del contenuto password 
            password = ''.join(random.choice(chars) for i in range(lunghezza_psw))
            print(password)
    
            # scrittrua password nel file csv riga per riga
            writer.writerow([password])

pswGenerator()

input("Press enter to exit...")

