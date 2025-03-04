import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{"imie": "Przemek", "mgs": "Hello World!"}',
                          rv.data)

    def test_msg_with_output_json(self):
        imie = "Alicja"
        msg = "Hello World!"

        expected = {}
        expected['imie'] = imie
        expected['mgs'] = msg
        json_expected = json.dumps(expected)

        rv = self.app.get('/?name='+imie+'&&output=json')
        self.assertEquals(json_expected,rv.data)
        #self.assertEquals('{"imie": "'+imie+'", "mgs": "Hello World!"}',
        #                  rv.data)
    def test_msg_with_output_xml(self):
        imie = "Alicja"
        msg = "Hello World!"
        rv = self.app.get('/?name='+imie+'&&output=xml')
        self.assertEquals("<greetings> <name>"+imie+"</name><msg>"+msg+"</msg></greetings>",rv.data)
