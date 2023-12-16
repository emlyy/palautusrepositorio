class ConsoleIO:
    def kirjoita(self, teksti):
        print(teksti)

    def pelaajan_syote(self, teksti):
        return input(teksti)

    def ekan_siirto(self):
        return self.pelaajan_syote("Ensimmäisen pelaajan siirto: ")
    
    def toisen_siirto(self):
        return self.pelaajan_syote("Toisen pelaajan siirto: ")

    def tietokoneen_siirto(self, siirto):
        return self.kirjoita(f"Tietokone valitsi: {siirto}")
