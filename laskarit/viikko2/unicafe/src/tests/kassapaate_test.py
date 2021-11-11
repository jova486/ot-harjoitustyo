import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

EDULLINEN = 240
MAUKAS = 400

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa_ja_alustettu_oikein(self):
        self.assertNotEqual(self.kassapaate, None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maksu_riittava_kassa_ja_vaihtoraja_oikein(self):
        maksu = 500
        vaihtoraha=self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+EDULLINEN)
        self.assertEqual(vaihtoraha, maksu - EDULLINEN)
        self.assertEqual(vaihtoraha, maksu - EDULLINEN)
        self.assertEqual(self.kassapaate.edulliset, 1)
        

        maksu = 500
        vaihtoraha=self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+MAUKAS+EDULLINEN)
        self.assertEqual(vaihtoraha, maksu - MAUKAS)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_riittava_kassa_ja_palautus_oikein(self):
        maksu = 100
        palautus=self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(palautus, maksu)
        self.assertEqual(self.kassapaate.edulliset, 0)

        palautus=self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(palautus, maksu)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_rahaa_kassa_ja_vaihtoraja_oikein(self):
        maksukortti = Maksukortti(10000)
        b=self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertTrue(b)

       
        b=self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertTrue(b)

    def test_kortilla_ei_rahaa_kassa_ja_vaihtoraja_oikein(self):
        maksukortti = Maksukortti(100)
        b=self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertFalse(b)

       
        b=self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertFalse(b)

    def test_lataa_rahaa_kortille_oikeat_summat(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,-1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(maksukortti.saldo, 100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(maksukortti.saldo, 200)
        

    """Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla"""


   
"""def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= 240:
            self.kassassa_rahaa = self.kassassa_rahaa + 240
            self.edulliset += 1
            return maksu - 240
        else:
            return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= 400:
            self.kassassa_rahaa = self.kassassa_rahaa + 400
            self.maukkaat += 1
            return maksu - 400
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= 240:
            kortti.ota_rahaa(240)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= 400:
            kortti.ota_rahaa(400)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return
"""