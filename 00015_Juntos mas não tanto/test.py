class Test(unittest.TestCase):

  def test_juntar_super_califragilistico_espialidoso_retorna_supercalifragilisticoespialidoso(self):
    self.assertEqual(juntar("", ["super", "califragilistico", "espialidoso"]), "supercalifragilisticoespialidoso")
    
  
  def test_juntar_quadri_motor_retorna_quadrimotor(self):
    self.assertEqual(juntar("", ["quadri", "motor"]), "quadrimotor")
    
  def test_juntar_olá_mundo_com_um_espaço_retorna_olá_mundo(self):
    self.assertEqual(juntar(" ", ["olá", "mundo"]), "olá mundo")
    
      
  def test_juntar_olá_mundo_com_uma_vírgula_retorna_olá_vírgula_mundo(self):
    self.assertEqual(juntar(",", ["olá", "mundo"]), "olá,mundo")
    
    
  
    
    