class Test(unittest.TestCase):

  def test_juntar_super_califragilistico_espialidoso_retorna_supercalifragilisticoespialidoso(self):
    self.assertEqual(juntar(["super", "califragilistico", "espialidoso"]), "supercalifragilisticoespialidoso")
    
  def test_juntar_lista_vazia_retorna_string_vazio(self):
    self.assertEqual(juntar([]), "")
    
  
  def test_juntar_quadri_motor_retorna_quadrimotor(self):
    self.assertEqual(juntar(["quadri", "motor"]), "quadrimotor")