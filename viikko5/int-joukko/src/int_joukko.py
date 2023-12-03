KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.numero_lista = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, numero):
        for i in range(self.alkioiden_lkm):
            if numero == self.numero_lista[i]:
                return True
        return False

    def lisaa(self, numero):
        if self.alkioiden_lkm == 0:
            self.numero_lista[0] = numero
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(numero):
            self.numero_lista[self.alkioiden_lkm] = numero
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.numero_lista):
                self.kasvata_listaa()

            return True

        return False

    def kasvata_listaa(self):
        vanha_lista = self.numero_lista
        self.kopioi_lista(self.numero_lista, vanha_lista)
        self.numero_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(vanha_lista, self.numero_lista)
    
    def poista(self, numero):
        for i in range(self.alkioiden_lkm):
            if numero == self.numero_lista[i]:
              # siis luku löytyy tuosta kohdasta :D
                self.numero_lista[i] = 0
                if self.siirra_alkiot(i):
                    return True
                break
        return False

    def siirra_alkiot(self, kohta):
        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                self.numero_lista[j] = self.numero_lista[j + 1]

            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, vanha_lista, uusi_lista):
        for i in range(len(vanha_lista)):
            uusi_lista[i] = vanha_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        self.kopioi_lista(self.numero_lista[:len(taulu)], taulu)

        return taulu

    @staticmethod
    def yhdiste(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.to_int_list()
        b_taulu = lista_b.to_int_list()

        lisaa_taulu_joukkoon(joukko, a_taulu)
        lisaa_taulu_joukkoon(joukko, b_taulu)

        return joukko

    @staticmethod
    def leikkaus(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.to_int_list()
        b_taulu = lista_b.to_int_list()

        for alkio in a_taulu:
            if alkio in b_taulu:
                joukko.lisaa(alkio)

        return joukko

    @staticmethod
    def erotus(lista_a, lista_b):
        joukko = IntJoukko()
        a_taulu = lista_a.to_int_list()
        b_taulu = lista_b.to_int_list()

        lisaa_taulu_joukkoon(joukko, a_taulu)

        for i in range(len(b_taulu)):
            joukko.poista(b_taulu[i])

        return joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuotos = "{"
        tuotos += str(self.numero_lista[0])
        if self.alkioiden_lkm != 1:
            for i in range(1, self.alkioiden_lkm):
                tuotos += ", "
                tuotos += str(self.numero_lista[i])
        tuotos += "}"
        return tuotos

def lisaa_taulu_joukkoon(joukko, taulu):
        for i in range(len(taulu)):
            joukko.lisaa(taulu[i])
