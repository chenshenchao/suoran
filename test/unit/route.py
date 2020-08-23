from unittest import TestCase, skip
from test.mock import controller

class RouteTest(TestCase):
    '''
    '''
    def test_controller(self):
        tc = controller.TestController()
        r = tc.index()
        self.assertEqual(r, 'index')
        