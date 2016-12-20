# coding: utf-8
import unittest
from bs4 import BeautifulSoup
from bs4_srcset import bs4_srcset

class UtilsTests(unittest.TestCase):
    def test_get_img_url_from_srcset(self):
        html = '<td colspan="2" style="text-align:center"><a href="/wiki/File:District-Massachusetts.png" class="image"><img alt="District-Massachusetts.png" src="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/150px-District-Massachusetts.png" width="150" height="148" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/225px-District-Massachusetts.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/300px-District-Massachusetts.png 2x" data-file-width="600" data-file-height="593" /></a></td>'
        soup = BeautifulSoup(html, 'html5lib')
        image_srcset = soup.find('img').get('srcset')

        image_url = bs4_srcset.get_img_url_from_srcset('', ['1.5x'])
        self.assertEqual(image_url, None)

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, ['1.5x'])
        self.assertEqual(image_url, '//upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/225px-District-Massachusetts.png')

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, ['2x'])
        self.assertEqual(image_url, '//upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/300px-District-Massachusetts.png')

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, ['1x', '1.5x'])
        self.assertEqual(image_url, '//upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/225px-District-Massachusetts.png')

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, ['2x', '1.5x'])
        self.assertEqual(image_url, '//upload.wikimedia.org/wikipedia/commons/thumb/9/93/District-Massachusetts.png/300px-District-Massachusetts.png')

# python -m unittest discover -s tests -p "*_tests.py"
