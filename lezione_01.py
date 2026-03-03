#Lezione 1 / 2 / 3
# 23/02 25/02
#costruttori normali/ costruttori modificati/ metodi di istanza, di classe, statici
#proteggere le variabili (come private su java @proprerty e @nomeMetodo.setter) e segnalare errori se ce ne sono,
# durante il cambio di variabile.


#from unicodedata import name (non so se si debba usare)


class Prodotto:
    #ATTRIBUTO DI CLASSE ->un attributo specifico uguale per una classe (per tutti gli oggetti)
    aliquota_iva = 0.22 #N.B. se dopo la modifico sotto, sotto quella modificata usa il numero modificato
    #prende quindi l'ultimo valore che vede.

    def __init__(self, name: str, price: float, quantity: int, supplier:str):
        #ATTRIBUTI DI ISTANZA-> più attributi, che cambiano da oggetto a oggetto
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
class Abbonamento(Prodotto):

    def __init__(self, name: str, prezzo_mensile: float, mesi: int):
        super().__init__(name = name, price = prezzo_mensile, quantity = 1, supplier= None)
        self.mesi = mesi

    def prezzo_finale(self):
        return self.price * self.mesi

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

print("--------------------------------------------------------------")
#Altro DECORATORE
from dataclasses import dataclass
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float
@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str

@dataclass
class RigaOrdine:
    prodotto: ProdottoRecord
    quantità: int

    def totale_riga(self):
        return self.prodotto.prezzo_unitario * self.quantità

@dataclass
class Ordine:
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga for r in self.righe)
    def totale_lordo(self, aliquota_iva):
        return self.totale_netto()* (1+aliquota_iva)
    def numero_righe(self):
        return len(self.righe)

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@live.it", "Gold")
p1 = ProdottoRecord("laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)

print("Numero righe dell'ordine", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo: ", ordine.totale_lordo())

print("-------------------------------------------------------------------")


#dato che abbiamo visto i getter e i setter, modifichiamo "self.categoria = categoria" in modo che
#sia protetta ( si possa cambiare solo in "Gold" "Silver" "Bronze")
class Cliente:
    def __init__(self, nome , mail , categoria):
        self.nome = nome
        self.mail = mail
        self._categoria = None
        self.categoria = categoria

    #getter
    @property
    def categoria(self):
        return self._categoria
    #setter
    @categoria.setter
    def categoria(self,new_categoria):
        categorie_valide = {"Gold", "Silver", "Bronze"}
        if new_categoria not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida, si può scegliere solo: Gold, Silver, Bronze")
        self._categoria = new_categoria


    def descrizione(self):
        return f"Cliente: {self.nome} ({self.categoria}) - {self.mail}"

#stampiamo e creiamo un normale cliente
c1 = Cliente(nome="Mario Bianchi", mail="mario.bianchi@polito.it", categoria="Gold")
print(c1.descrizione())
#qui verifico che il controllo getter/setter funzioni; metto una categoria che non esiste "Platinum"

#c2 = Cliente("Luigi","luigi01@live.it", "Platinum") #è commentato perchè visualizza un errore.
#print(c2.descrizione())

#CHIAMATA METODO DI ISTANZA
print(f"Il valore netto del ''myproduct1'' è {myproduct1.valore_netto()}") # ogetto specifico.metodo()

#CHIAMATA METODO DI CLASSE
p3 = Prodotto.costruttore_con_quantita_uno("Auricolari",200.0, "ABC") #nome_classe.metodo(...)


#CHIAMATA METODO DI STATICO
print(f"Prezzo scontato di myproduct1 -> {Prodotto.applica_sconto(myproduct1.price,0.15)}") #nome_classe.metodo()




print(f" print(myproduct1) dopo aver settato il dunder '__str__' sotto la classe -->  {myproduct1}")

myproduct1_copy = Prodotto( name= "Laptop" , price= 1200.0, quantity=12, supplier="ABC" )

print(f"Utilizzando il dunder __eq__ verifico che myproduct1 sia uguale alla sua copia myproduct1copy si fa semplicemente "
      f"con '==':  {myproduct1 == myproduct1_copy}")
print(f"adesso ne confronto 2 diversi: {myproduct1 == myproduct2}")


print("fine")







