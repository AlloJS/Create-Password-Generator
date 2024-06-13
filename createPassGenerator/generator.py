import random
from .exceptions import GetErrorPass

def strong_pass(length=25):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!|^$&£-_()][}@#*{'
    all_characters = upper_case + lower_case + numbers + symbols
    
    if length < 10:
        raise GetErrorPass("La lunghezza della password deve essere almeno 10 caratteri")
    
    return ''.join(random.sample(all_characters * 50, length))

def get_user_data():
    platform = input("Inserisci la piattafarma per cui vuoi registrare l'account: ")
    username = input("Inserisci username da usare: ")
    lenght_pass =  int(input("Inserisci la lunghezza della password che vuoi creare (Un minimo di 10 caratteri): "))
    pasword = strong_pass(lenght_pass)
    
    return {
        "platform" : platform,
        "username" : username,
        "pasword" : pasword
    }
    
def save_user_data_to_file(data,filename="account_data.txt"):
        with open(filename,'a') as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
    

def main():
    user_data = get_user_data()
    save_user_data_to_file(user_data)
    print(f"I tuoi dati sono stati salvati correttamente in  account_data_data.txt")    
