import random
from .exceptions import GetErrorPass

def strongPass(length=25):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!|^$&£-_()][}@#*{'
    all_characters = upper_case + lower_case + numbers + symbols
    
    if length < 10:
        raise GetErrorPass("La lunghezza della password deve essere almeno 10 caratteri")
    
    return ''.join(random.sample(all_characters * 50, length))
