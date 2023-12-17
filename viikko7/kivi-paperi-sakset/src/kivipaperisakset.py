class KiviPaperiSakset:
    def __init__(self, io, tuomari, tekoaly):
        self.io = io
        self.tuomari = tuomari
        self.tekoaly = tekoaly

    def pelaa(self):
        ekan_siirto = self.io.ekan_siirto()
        tokan_siirto = self.tokan_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self.io.kirjoita(self.tuomari)

            ekan_siirto = self.io.ekan_siirto()
            tokan_siirto = self.tokan_siirto(ekan_siirto)

        self.io.kirjoita("Kiitos!")
        self.io.kirjoita(self.tuomari)

    def tokan_siirto(self, ekan_siirto):
        pass

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
