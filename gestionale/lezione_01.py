from prodotti import Prodotto, crea_prodotto_standard
import networkx as nx
#VIRTUAL ENVIROMENTS una cartella in cui ci sono solo le librerie che utilizzo
# così posso usare la classe prodotto come se fosse qui




print("====================================================================================")
p1 = Prodotto("Ebook Reader", 120.0, 1, "AAA")
p2 = crea_prodotto_standard("Tablet",750.0)

print(p1)
print(p2)

#MODI PER IMPORTARE

from prodotti import ProdottoScontato as ps #rinomina la classe
p3 = ps("Auricolari", 230, 1, "ABC", 0.10)

import prodotti #importa tutto

p4 = prodotti.ProdottoScontato("Auricolari", 230, 1, "ABC", 0.10)

#IMPORTANTE: quando importo da un altro file, viene importato anche la console del file, un
# buon file importato, non deve avere print (anche se i test li devo fare, quindi magari li elimino)
#oppure usare il def _test_prova dentro il file che devo importare

from gestionale.cliente import Cliente
c1 = Cliente("Mario", "mario@...", "Gold")
print(c1)

print("====================================================================================")
















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
class Ordine: #il simbolo blu ci avverte che qualcuno ha fatto una sottoclasse
    righe: list[RigaOrdine]
    cliente: ClienteRecord

    def totale_netto(self):
        return sum(r.totale_riga() for r in self.righe)
    def totale_lordo(self, aliquota_iva):
        return self.totale_netto()* (1+aliquota_iva)
    def numero_righe(self):
        return len(self.righe)

@dataclass
class OrdineConSconto(Ordine):
    sconto_percentuale: float

    def totale_scontato(self):
        return self.totale_lordo()* (1-self.sconto_percentuale)
    def totale_netto(self):
        netto_base = super().totale_netto()
        return netto_base*(1-self.sconto_percentuale)



cliente1 = ClienteRecord("Mario Rossi", "mariorossi@live.it", "Gold")
p1 = ProdottoRecord("laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)

ordine = Ordine([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1,2), RigaOrdine(p2,10)], cliente1, 0.10)


print(ordine)
print("Numero righe dell'ordine", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo: ", ordine.totale_lordo(0.22))

print("-------------------------------------------------------------------")




#dato che abbiamo visto i getter e i setter, modifichiamo "self.categoria = categoria" in modo che
#sia protetta ( si possa cambiare solo in "Gold" "Silver" "Bronze")


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







