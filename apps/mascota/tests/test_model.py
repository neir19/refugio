from django.test import TestCase
from apps.mascota.models import Mascota, Vacuna

class MascotaTestCase(TestCase):
  def setUp(self):
    Mascota.objects.create(nombre="lola", sexo="femenino",edad_aproximada=2,fecha_recate="2020-06-19")
    Mascota.objects.create(nombre="lupita", sexo="Masculino",edad_aproximada=1,fecha_recate="2020-04-19")
  def test_mascotas_sexo(self):
    """Las mascotas pueden tener el sexo correctamente definido"""
    lola=Mascota.objects.get(sexo="Masculino")
    lupita=Mascota.objects.get(sexo="Femenino")

    self.assertEqual(lola.sexo,lupita.sexo,"femenin0")
    self.assertEqual(lupita.sexo,lola.sexo,"masc")