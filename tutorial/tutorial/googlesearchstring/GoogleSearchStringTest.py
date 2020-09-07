import unittest
from tutorial.tutorial.googlesearchstring import GoogleSearchString

class GoogleSearchStringTest(unittest.TestCase):

    gsst = GoogleSearchString

    def test_search_query(self):
        query = ['"my big dog"',
                 '"my big" dog',
                 'my big dog',
                 ]
        ref_url = ['http://www.google.com/search?as_epq=my+big+dog',
                   'http://www.google.com/search?q="my+big"+dog&oq="my+big"+dog',
                   'http://www.google.com/search?q=my+big+dog'
                   ]

        for i in range(query.__len__()):
            url = self.gsst().search_query(query[i])
            self.assertEqual(url, ref_url[i])

    def test_advanced_options(self):
        url = self.gsst(omitted_res_filter=True).search_query('my big dog')
        ref_url = 'http://www.google.com/search?q=my+big+dog&filter=0'

        self.assertEqual(url, ref_url)

    def test_object_kwargs(self):
        obj = GoogleSearchString(omitted_res_filter=True)
        print(obj.omitted_res_filter, '\n', obj.search_query('kk'))



if __name__ == '__main__':
    unittest.main()
