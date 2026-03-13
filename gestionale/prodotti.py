#Lezione 1 / 2 / 3
# 23/02 25/02
#costruttori normali/ costruttori modificati/ metodi di istanza, di classe, statici
#proteggere le variabili (come private su java @proprerty e @nomeMetodo.setter) e segnalare errori se ce ne sono,
# durante il cambio di variabile.


#from unicodedata import name (non so se si debba usare)


class Prodotto:
    #------------------ATTRIBUTO DI CLASSE ->un attributo specifico uguale per una classe (per tutti gli oggetti)
    aliquota_iva = 0.22 #N.B. se dopo la modifico sotto, sotto quella modificata usa il numero modificato
    #prende quindi l'ultimo valore che vede.

    def __init__(self, name: str, price: float, quantity: int, supplier:str):
        #------------------------ATTRIBUTI DI ISTANZA-> più attributi, che cambiano da oggetto a oggetto
        self.name = name
        self._price = None #per getter e setter
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

    # equivalente di getter
    @property
    def price(self):
        return self._price
    #equivalente dei setter

    @price.setter    #serve più che altro a fare dei controlli, per esempio controllare se il prezzo è negativo
    def price(self, valore):
        if valore <0:
            raise ValueError("Attenzione il prezzo non può essere negativo")
        self._price = valore

    # DUNDER METHODS: metodi importanti(chiamati speciali) con la forma __metodo__ da imparare
    # servono molto spesso per fare operazioni con oggetti: stampa, confronto, ecc.

    # STAMPA DELL'OGGETTO, per l'utente
    def __str__(self):
        return (f"{self.name}, disponibili {self.quantity} pezzi, a {self.price}€")

    # STAMPA DELL'OGGETTO, per il programmatore (schematico) NEL DEBUGGER.
    #    def __init__(self, name: str, price: float, quantity: int, supplier:str):
    def __repr__(self):
        return (f"nome = {self.name}, prezzo = {self.price}, quantità = {self.quantity}, supplier = {self.supplier} ")

    #VEDERE SE SONO UGUALI 2 OGGETTI
    def __eq__(self, other:object): #object permette il paragone con qualsiasi oggetto
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    #CONFRONTARE IN QUALCHE MODO 2 OGGETTI
    def __lt__(self, other: "Prodotto") -> bool:
        return self.price < other.price #ordine crescente di prezzo dunque

    def prezzo_finale(self):
        return self.price*(1 + self.aliquota_iva)


    #EREDITARIETA'
    # faccio una classe che ha TUTTE le caratteristiche di Prodotto, e TUTTI i metodi
    # ma è specializzata: ha delle cose in più
    # attenzione non è come programmazione a oggetti, si può un minimo modificare
    # vedi classe Servizio, dove sono stati modificati alcuni campi del padre
    #per esempio cambiato da prezzo a tariffa oraria, oppure messo un None
    # perchè non aveva quella caratteristica

class ProdottoScontato(Prodotto):
    def __init__(self,name: str, price: float, quantity: int, supplier:str, sconto_percento: float):
            #Prodotto.__init__()
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self)-> float:
        return self.valore_lordo()* (1- self.sconto_percento/100)

class Servizio(Prodotto):

    def __init__(self,name: str, tariffa_oraria: float, ore: int ):
        super().__init__(name = name, price= tariffa_oraria, quantity=1, supplier=None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore
    # si introduce il polimorfismo, chiamiamo lo stesso metodo prezzo_finale (per prodotto, servizio e prodottoscontato)
    # ma il contenuto cambia da oggetto a oggetto

class Abbonamento(Prodotto):

    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        super().__init__(name = name, price = prezzo_mensile, quantity = 1, supplier= None)
        self.mesi = mesi

    def prezzo_finale(self):
        return self.price * self.mesi

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome, prezzo, 1, None)


myproduct1 = Prodotto( name= "Laptop" , price= 1200.0, quantity=12, supplier="ABC" )
print(f"Nome Prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

myproduct2 = Prodotto( name= "Mouse" , price= 10, quantity=25, supplier="CDE" )
print(f"Nome Prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

my_product_scontato= ProdottoScontato("Auricolari", 320.0, 1, "ABC", 10)
my_service = Servizio("Consulenza", 100, 3 )

my_list = [myproduct1, myproduct2, my_service, my_product_scontato]
my_list.sort() # abbiamo deciso che l'ordine è crescente per prezzo dai dunder

for elemento in my_list:
    print(f"- {elemento}") #anche se sono oggetti diversi, si possono stampare ordinare e inserire nelle liste




#ESERCIZIO creo una classe abbonamento che abbia nome prezzomensile mesi e abbia un prezzo_finale


abb = Abbonamento("Software gestionale", 30.0, 24 )

my_list.append(abb)

for element in my_list:
    print(f"nome: {element.name}, prezzo: {element.prezzo_finale()}")



def calcola_totale(elementi):
    tot = 0
    for e in elementi:
        tot += e.prezzo_finale()
    return tot

#PROTOCOLLO serve per dire al programmatore che caratteristiche deve avere un elemento
#per esempio nel for precedente
from typing import Protocol

class HaPrezzoFinale(Protocol): #significa: creo una classe HaPrezzoFinale
    def prezzo_finale(self) -> float: #che deve avere un metodo prezzo_finale
        ...
def calcola_totale(elementi: list[HaPrezzoFinale]) -> float: #significa che gli "elementi" hanno prezzo_finale
    return sum(e.prezzo_finale() for e in elementi)