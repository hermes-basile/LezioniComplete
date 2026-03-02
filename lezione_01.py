#Lezione 1 / 2
# 23/02 25/02
#costruttori normali/ costruttori modificati/ metodi di istanza, di classe, statici
#proteggere le variabili (come private su java) e segnalare errori se ce ne sono, durante il cambio di variabile.


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



myproduct1 = Prodotto( name= "Laptop" , price= 1200.0, quantity=12, supplier="ABC" )
print(f"Nome Prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

myproduct2 = Prodotto( name= "Mouse" , price= 10, quantity=25, supplier="CDE" )
print(f"Nome Prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")



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
c2 = Cliente("Luigi","luigi01@live.it", "Platinum")
print(c2.descrizione())

#CHIAMATA METODO DI ISTANZA
print(f"Il valore netto del ''myproduct1'' è {myproduct1.valore_netto()}") # ogetto specifico.metodo()

#CHIAMATA METODO DI CLASSE
p3 = Prodotto.costruttore_con_quantita_uno("Auricolari",200.0, "ABC") #nome_classe.metodo(...)


#CHIAMATA METODO DI STATICO
print(f"Prezzo scontato di myproduct1 -> {Prodotto.applica_sconto(myproduct1.price,0.15)}") #nome_classe.metodo()