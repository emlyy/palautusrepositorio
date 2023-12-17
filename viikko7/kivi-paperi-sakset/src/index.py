from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from console_io import ConsoleIO
from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class PeliTehdas:
    def __init__(self):
        self.pelit = {
            "a": KPSPelaajaVsPelaaja(ConsoleIO(), Tuomari(), None),
            "b": KPSTekoaly(ConsoleIO(), Tuomari(), Tekoaly()),
            "c": KPSParempiTekoaly(ConsoleIO(), Tuomari(), TekoalyParannettu(10))
        }

    def hae(self, peli):
        if peli in self.pelit:
            return self.pelit[peli]
        return None


def main():
    pelit = PeliTehdas()
    IO = ConsoleIO()
    while True:
        vastaus = IO.pelaajan_syote("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              "\n ")

        IO.kirjoita(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

        peli = pelit.hae(vastaus)

        if peli:
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
