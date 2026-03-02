#Lezione 1
# 23/02
#from unicodedata import name (non so se si debba usare)


class Prodotto:
    #ATTRIBUTO DI CLASSE ->un attributo specifico uguale per una classe (per tutti gli oggetti)
    aliquota_iva = 0.22

    def __init__(self, name: str, price: float, quantity: int, supplier:str):
        #ATTRIBUTI DI ISTANZA-> più attributi, che cambiano da oggetto a oggetto
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    #METODO DI ISTANZA ->  serve per un singolo oggetto
    def valore_netto(self):
        return self.price * self.quantity

    def valore_lordo(self):
        netto = self.price * self.quantity
        lordo = netto*(1+self.aliquota_iva)
        return lordo


    #METODO DI CLASSE -> serve per l'intera classe (oggetto in generale non specifico)
    @classmethod
    def costruttore_con_quantita_uno(cls, name: str, price: float, supplier:str ):#serve per creare dei costruttori alternativi, per esempio quando ho una quantità = 1
        cls(name, price, 1, supplier)


    #METODO STATICO -> di base non si riferisce a niente, è un metodo indipendente
    @staticmethod
    def applica_sconto(prezzo, percentuale):
        return prezzo*(1-percentuale)
    #chiamata metodo ->



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
        return f"Cliente: {self.nome} ({self.categoria}) - {self.mail}"

c1 = Cliente(nome="Mario Bianchi", mail="mario.bianchi@polito.it", categoria="Gold")
print(c1.descrizione())

#CHIAMATA METODO DI ISTANZA
print(f"Il valore netto del ''myproduct1'' è {myproduct1.valore_netto()}") # ogetto specifico.metodo

#CHIAMATA METODO DI CLASSE


#CHIAMATA METODO DI STATICO