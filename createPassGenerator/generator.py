import random
from exceptions import GetErrorPass

def strongPass(lenght=25):
    lower_case = 'abcdefghijklmnopqrstuvwz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWZ'
    numbers = '0123456789'
    simbols ='!|^$&£-_()][}@#*{'
    all_charatters = upper_case + lower_case + numbers + simbols
    
    if lenght < 10:
        raise GetErrorPass("Il numero inserito deve essere almeno 10")
    
    return '' .join(random.sample(all_charatters * 50, lenght))


print(strongPass(1))