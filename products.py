#一維清單
# products = []
# while True:
#     name = input('請輸入商品名稱：')
#     if name == 'q':
#         break
#     products.append(name)
# print(products)
#二維清單_版本1
# products = []
# while True:
#     name = input('請輸入商品名稱：')
#     if name == 'q':
#         break
#     price = input('請輸入商品價格：')
#     p = []
#     p.append(name)
#     p.append(price)
#     products.append(p)
# print(products)
#二維清單_版本2
products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    p = [name, price]
    products.append(p)
print(products)
#二維清單_版本3
products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    products.append([name, price])
print(products)
