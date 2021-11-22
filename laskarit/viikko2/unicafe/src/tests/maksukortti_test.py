import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 100.0")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10000)
        self.assertEqual(str(self.maksukortti), "saldo: 200.0")

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11000)
        self.assertEqual(str(self.maksukortti), "saldo: 100.0")

    def test_ota_rahaa_palauttaa_True_jos_rahat_riittivat(self):
        b=self.maksukortti.ota_rahaa(5000)
        self.assertTrue(b)

    def test_ota_rahaa_palauttaa_False_jos_rahat_(self):
        b=self.maksukortti.ota_rahaa(15000)
        self.assertFalse(b)
    
    