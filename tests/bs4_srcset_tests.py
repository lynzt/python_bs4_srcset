# coding: utf-8
import unittest
from bs4 import BeautifulSoup
from bs4_srcset import bs4_srcset

class UtilsTests(unittest.TestCase):
    def test_get_img_url_from_srcset(self):
        html = '<img width="264" height="264" src="https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-264x264.png" class="attachment-executive-image size-executive-image wp-post-image" alt="CEODenise_CampbellSoupCompany2016" srcset="https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-264x264.png 264w, https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-150x150.png 150w, https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-300x300.png 300w, https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-145x145.png 145w, https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016.png 362w" sizes="(max-width: 264px) 100vw, 264px" />'
        soup = BeautifulSoup(html, 'html5lib')
        image_srcset = soup.find('img').get('srcset')

        image_url = bs4_srcset.get_img_url_from_srcset('', {'min':150})
        self.assertEqual(image_url, None)

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, {})
        self.assertEqual(image_url, 'https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-264x264.png')

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, {'min': 150, 'max': 150})
        self.assertEqual(image_url, 'https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-150x150.png')

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, {'min': 300})
        self.assertEqual(image_url, 'https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-300x300.png')

        image_url = bs4_srcset.get_img_url_from_srcset(image_srcset, {'max': 200})
        self.assertEqual(image_url, 'https://www.campbellsoupcompany.com/wp-content/uploads/sites/31/2016/04/CEODenise_CampbellSoupCompany2016-150x150.png')

# python -m unittest discover -s tests -p "*_tests.py"
