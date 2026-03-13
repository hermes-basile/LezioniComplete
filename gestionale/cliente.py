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

 # stampiamo e creiamo un normale cliente
def _test_modulo():
    c1 = Cliente(nome="Mario Bianchi", mail="mario.bianchi@polito.it", categoria="Gold")
    print(c1.descrizione())

if __name__ == "__main__":
    _test_modulo()