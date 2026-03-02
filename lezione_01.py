#Lezione 1
# 23/02
#from unicodedata import name (non so se si debba usare)


class Prodotto:
    aliquota_iva = 0.22 #si chiama variabile di classe, ed è uguale per tutti gli oggetti Prodototre

    def __init__(self, name: str, price: float, quantity: int, supplier:str):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

def valore(self):
    return self.price * self.quantity


myproduct1 = Prodotto( name= "Laptop" , price= 1200.0, quantity=12, supplier="ABC" )
print(f"Nome Prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

myproduct2 = Prodotto( name= "Mouse" , price= 10, quantity=25, supplier="CDE" )
print(f"Nome Prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

class Cliente:
    def __init__(self, nome , mail , categoria):
        self.nome = nome
        self.mail = mail
        self.categoria = categoria

def descrizione(self):
    return f"Cliente: {self.name}  ({self.categoria}) - {self.mail}"