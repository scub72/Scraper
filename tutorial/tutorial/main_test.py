from tutorial.tutorial.items import Product
from scrapy.loader import ItemLoader
il = ItemLoader(item=Product())
il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
il.add_value('price', [u'&euro;', u'<span>1000</span>'])
print(il.load_item())

nn = 'naaa'
