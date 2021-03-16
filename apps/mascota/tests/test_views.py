from django.test import TestCase

class viewTestCase(TestCase):
  def text_index_load_correct(self):
    """La carga del index es correcta"""
    response=self.client.get('your:server_ip_8000')
    self.assertEqual(response.status_code,404)
