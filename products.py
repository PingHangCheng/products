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
# products = []
# while True:
#     name = input('請輸入商品名稱：')
#     if name == 'q':
#         break
#     price = input('請輸入商品價格：')
#     p = [name, price]
#     products.append(p)
# print(products)
#二維清單_版本3
products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])
print(products)

for p in products:
    # print(p[0]) 會印出小清單的商品名稱
    print(p[0], "的價格是", p[1] )

# with open ('product.csv', 'w') as f:
#     f.write('商品, 價格 \n')
#     for p in products:
#         f.write(p[0] + ',' + str(p[1]) + '\n')

#如果出現亂碼時，沒有亂碼，就不用，寫入檔案時加入encoding='utf-8' 來解決中文字變亂碼問題, = 兩邊不要空格
with open ('product.csv', 'w', encoding='utf-8') as f:
    f.write('商品, 價格 \n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
