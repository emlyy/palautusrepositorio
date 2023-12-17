from kivipaperisakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):
    def tokan_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        self.io.tietokoneen_siirto(tokan_siirto)
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto
