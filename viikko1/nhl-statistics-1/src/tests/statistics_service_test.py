import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_palauttaa_pelaajan_jos_loytyy(self):
        pelaaja = self.stats.search("Semenko")
        self.assertEqual(pelaaja.goals, 4)
        self.assertEqual(pelaaja.team, "EDM")

    def test_search_ei_palauta_jos_ei_loydy(self):
        pelaaja = self.stats.search("emly")
        maalit = None
        if pelaaja:
            maalit = pelaaja.goals
        self.assertEqual(maalit, None)

    def test_team_palauttaa_listan_pelaajia(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)
        self.assertEqual(pelaajat[0].name, "Semenko")

    def test_top_palauttaa_parhaan_teho(self):
        paras = self.stats.top(1)
        self.assertEqual(paras[0].name, "Gretzky")

    def test_top_palauttaa_parhaat_listan(self):
        parhaat = self.stats.top(3,1)
        self.assertEqual([parhaat[0].name, parhaat[1].name, parhaat[2].name], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_palauttaa_parhaan_teho_ilman_parametria(self):
        paras = self.stats.top(1,1)
        self.assertEqual(paras[0].name, "Gretzky")

    def test_top_palauttaa_parhaat_listan_ilman_parametria(self):
        parhaat = self.stats.top(3)
        self.assertEqual([parhaat[0].name, parhaat[1].name, parhaat[2].name], ["Gretzky", "Lemieux", "Yzerman"])

    def test_sorted_by_assists(self):
        paras = self.stats.top(3,3)
        self.assertEqual(paras[1].name, "Yzerman")

    def test_sorted_by_goals(self):
        paras = self.stats.top(3,2)
        self.assertEqual(paras[0].name, "Lemieux")