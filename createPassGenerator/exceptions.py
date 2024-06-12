class GetErrorPass:
    
    def __init__(self, message="La lunghezza deve essere almeno di 10", value=None):
        self.message = message
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        if self.value is not None:
            return f'{self.message}. Valore inserito: {self.value}'
        return self.message 