class Test(unittest.TestCase):

  def test_sem_extremos_da_lista_4_5_10_2_3_retorna_a_lista_5_10_2(self):
    self.assertEquals(sem_extremos([4, 5, 10, 2, 3]), [5, 10, 2])
    
  def test_sem_extremos_da_lista_4_5_10_2_3_9_retorna_a_lista_5_10_2_9(self):
    self.assertEquals(sem_extremos([4, 5, 10, 2, 3, 9]), [5, 10, 2, 3])
    
  def test_sem_extremos_da_lista_4_5_10_retorna_a_lista_5(self):
    self.assertEquals(sem_extremos([4, 5, 10]), [5])
        
  def test_sem_extremos_da_lista_40_20_retorna_a_lista_vazia(self):
    self.assertEquals(sem_extremos([40, 20]), [])
    
  def test_extremos_da_lista_4_5_10_2_3_retorna_a_lista_4_3(self):
    self.assertEquals(extremos([4, 5, 10, 2, 3]), [4, 3])
    
  def test_extremos_da_lista_4_3_retorna_a_lista_4_3(self):
    self.assertEquals(extremos([4, 3]), [4, 3])
    
  def test_extremos_da_lista_1_2_5_retorna_a_lista_1_5(self):
    self.assertEquals(extremos([1, 2, 5]), [1, 5])      
