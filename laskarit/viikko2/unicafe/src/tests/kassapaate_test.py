import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassassa_rahaa_alku(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_edulliset_alku(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kassassa_maukkaat_alku(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisesti_kateisella_liian_pieni(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(220),220)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa)
        self.assertEqual(self.kassapaate.edulliset, alku_edulliset)
    
    def test_edullisesti_kateisella(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260),20)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa+240)
        self.assertEqual(self.kassapaate.edulliset, alku_edulliset+1)

    def test_maukkaasti_kateisella(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(404),4)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa+400)
        self.assertEqual(self.kassapaate.maukkaat, alku_edulliset+1)
    
    def test_maukkaasti_kateisella_liian_pieni(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300),300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, alku_edulliset)
    
    def test_edullisesti_kortilla_liian_pieni(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti),False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa)
        self.assertEqual(self.kassapaate.edulliset, alku_edulliset)
    
    def test_edullisesti_kortilla(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti),True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa)
        self.assertEqual(self.kassapaate.edulliset, alku_edulliset+1)

    def test_maukkaasti_kortilla(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti),True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, alku_edulliset+1)
    
    def test_maukkaasti_kortilla_liian_pieni(self):
        alku_rahaa = self.kassapaate.kassassa_rahaa
        alku_edulliset = self.kassapaate.edulliset
        maksukortti = Maksukortti(50)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti),False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, alku_edulliset)

    def test_lataa_kortille(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100100)
        self.assertEqual(str(maksukortti),"saldo: 2.0")

    def test_lataa_kortille_negatiivinen(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti,-1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(str(maksukortti),"saldo: 1.0")