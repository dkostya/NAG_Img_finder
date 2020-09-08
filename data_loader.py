import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'NAG_Img_finder.settings'

import django

django.setup()

print('Begin')

from nif.models import Product, Image
import json

with open('response.json', encoding='utf-8') as data_file:
    data = json.load(data_file)

item_num = 8683

for element in data:

    item_num -=1
    print(item_num)

    product = Product()
    product.title = (element['title'])
    product.sku = element['sku']
    product.save()
    for img in element['images']:

        image = Image()
        image.url = img
        image.product = product
        image.save()

print('Done')


