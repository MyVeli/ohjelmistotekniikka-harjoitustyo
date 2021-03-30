import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_alku_summa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_lataaminen(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
    
    def test_saldon_vahentaminen(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_saldon_vahentaminen_yli(self):
        self.maksukortti.ota_rahaa(50000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_saldo_vahentaminen_palautusarvo_true(self):        
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_saldo_vahentaminen_palautusarvo_false(self):        
        self.assertEqual(self.maksukortti.ota_rahaa(50000), False)