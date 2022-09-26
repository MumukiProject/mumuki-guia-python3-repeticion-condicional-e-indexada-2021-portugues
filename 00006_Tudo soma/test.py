class Test(unittest.TestCase):

  def test_produtório_de_10_2_3_é_60(self):
    self.assertEquals(produtorio([10, 2, 3]), 60)

  def test_produtório_de_3_3_2_4_é_72(self):
    self.assertEquals(produtorio([3, 3, 2, 4]), 72)

  def test_produtório_de_8_é_8(self):
    self.assertEquals(produtorio([8]), 8)

  def test_produtório_de_1_a_9_é_362880(self):
    self.assertEquals(produtorio(range(1, 10)), 362880)

  def test_produtório_de_6_é_6(self):
    self.assertEquals(produtorio([6]), 6)

  def test_produtório_de_lista_vazia_é_1(self):
    self.assertEquals(produtorio([]), 1)