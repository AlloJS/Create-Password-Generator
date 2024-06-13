class GetErrorPass(Exception):
    
    def __init__(self, message="La lunghezza deve essere almeno di 10", value=None):
        self.message = message
        self.value = value

def strong_pass(length):
    """Genera una password sicura di lunghezza specificata."""
    if length < 10:
        raise GetErrorPass("La lunghezza della password deve essere almeno 10 caratteri")

try:
    password = strong_pass(5)
except GetErrorPass as error:
    print("Errore:", error.message)
    print("Valore:", error.value)
