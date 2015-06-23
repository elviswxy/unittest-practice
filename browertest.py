__author__ = 'elvis'

from test_helpers import BrowserTestCase

class YourTestCase(BrowerTestCase):

    def setUp(self):
        self.brower = self.start_brower("Firefox")

    def test_page_loads(self):
        self.brower.get('127.0.0.1:8080')

        self.assertIn("Hello, World", self.body_text)

if __name__ == '__main__':
    BrowerTestCase.main()