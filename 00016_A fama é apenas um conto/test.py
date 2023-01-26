class Test(unittest.TestCase):

  def test_quantas_vezes_treino_o_suficiente_com_35_40_32_60_é_4(self):
    self.assertEquals(quantas_vezes_treinou_o_suficiente([35, 40, 32, 60]), 4)
    
  def test_quantas_vezes_treino_o_suficiente_com_15_45_90_0_é_2(self):
    self.assertEquals(quantas_vezes_treinou_o_suficiente([15, 45, 90, 0]), 2)
    