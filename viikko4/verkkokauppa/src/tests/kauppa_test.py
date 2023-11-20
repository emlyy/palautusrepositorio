import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

VIITE = 42
KAUPPA = "33333-44455"

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = VIITE
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 35
            if tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "banaani", 3)
            if tuote_id == 3:
                return Tuote(3, "omena", 4)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikealla_parametrilla(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("Matti", "12233")

        self.pankki_mock.tilisiirto.assert_called_with("Matti", VIITE, "12233", KAUPPA, 5)

    def test_tilisiirto_kahdella_eri_tuotteella(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Matti", "12233")

        self.pankki_mock.tilisiirto.assert_called_with("Matti", VIITE, "12233", KAUPPA, 8)

    def test_tilisiirto_kahdella_samalla_tuotteella(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Matti", "12233")

        self.pankki_mock.tilisiirto.assert_called_with("Matti", VIITE, "12233", KAUPPA, 6)

    def test_tilisiirto_tuote_puuttuu(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("Matti", "12233")

        self.pankki_mock.tilisiirto.assert_called_with("Matti", VIITE, "12233", KAUPPA, 3)

    def test_aloita_alusta_nollaa_ostoksen(self):
        ostoskori_mock = Mock()
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        id1 = ostoskori_mock.copy()
        kauppa.lisaa_koriin(2)
        kauppa.aloita_asiointi()
        id2 = ostoskori_mock

        self.assertNotEqual(id1, id2)

    def test_kauppa_pyytaa_aina_uuden_viite_numeron(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("Matti", "12233")

        self.pankki_mock.tilisiirto.assert_called_with("Matti", VIITE, "12233", KAUPPA, 3)
        self.viitegeneraattori_mock.uusi.return_value = 55
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("Matti", "12233")
        self.pankki_mock.tilisiirto.assert_called_with("Matti", 55, "12233", KAUPPA, 3)

    def test_poistettu_tuote_poistetaan_ostoskorista(self):
        ostoskori_mock = Mock()
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(2)
        kauppa.tilimaksu("Matti", "12233")

        self.pankki_mock.tilisiirto.assert_called_with("Matti", VIITE, "12233", KAUPPA, 5)
        
    def test_poistettu_tuote_palautetaan_varastoon(self):
        ostoskori_mock = Mock()
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(2)

        self.varasto_mock.palauta_varastoon.assert_called_with(Tuote(2, "banaani", 3))        

