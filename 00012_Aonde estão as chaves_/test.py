class Test(unittest.TestCase):

  def test_as_chaves_estรฃo_em_primeiro_lugar(self):
    self.assertEquals(onde_estao_as_chaves("๐๐ฅ๐"), 1)
    
  def test_as_chaves_estรฃo_em_segundo_lugar(self):
    self.assertEquals(onde_estao_as_chaves("๐๐๐ฅ"), 2)