from requests_html import HTMLSession
import pandas as pd

sourceFile = open('results.txt', 'w')

url = 'https://www.emag.ro/search/gratare-electrice/pret,intre-87-si-350/grill+electric/c'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)

products = r.html.xpath('//*[@id="card_grid"]', first=True)

index = 0 

for item in products.absolute_links:
    r = s.get(item)
    
    title = r.html.find('h1.page-title', first=True)
    price = r.html.find('p.product-new-price', first=True)
    
    index = index + 1

    print("No.: ", index, file = sourceFile)
    print("Title:", title.text, file = sourceFile)
    print("Price:", price.text, file = sourceFile)
    print("Link:", item, file = sourceFile)
    print("\n", file = sourceFile)












