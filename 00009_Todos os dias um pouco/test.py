class Test(unittest.TestCase):

  def test_todos_os_dias_um_pouco_com_35_40_32_60_é_True(self):
    self.assertTrue(todos_os_dias_um_pouco([35, 40, 32, 60]))
    
  def test_todos_os_dias_um_pouco_com_15_45_90_0_é_False(self):
    self.assertFalse(todos_os_dias_um_pouco([15, 45, 90, 0]))
    