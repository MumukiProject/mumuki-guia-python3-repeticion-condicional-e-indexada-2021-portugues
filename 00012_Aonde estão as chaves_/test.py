class Test(unittest.TestCase):

  def test_as_chaves_estão_em_primeiro_lugar(self):
    self.assertEquals(onde_estao_as_chaves("🔑🔥👓"), 1)
    
  def test_as_chaves_estão_em_segundo_lugar(self):
    self.assertEquals(onde_estao_as_chaves("👓🔑🔥"), 2)