from kivipaperisakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def tokan_siirto(self, ekan_siirto):
        return self.io.toisen_siirto()
