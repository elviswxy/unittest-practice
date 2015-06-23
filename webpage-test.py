__author__ = 'elvis'

import unittest
import urllib.request

class TestUrlHttpcode(unittest.TestCase):
   def setUp(self):
       urlinfo = ['http://my.openbidder/dsp/','http://my.openbidder/mockpublisher/']
       self.checkurl = urlinfo

   def test_ok(self):
       for m in self.checkurl:
           httpcode = urllib.request.urlopen(m).getcode()
           self.assertEqual(httpcode,200)

if __name__ == '__main__':
   unittest.main()