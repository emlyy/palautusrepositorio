from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):
    def tokan_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.io.tietokoneen_siirto(tokan_siirto)
        return tokan_siirto
