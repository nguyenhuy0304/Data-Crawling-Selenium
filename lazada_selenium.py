"""
•	Thông tin cần trích xuất:
o	Tên sản phẩm
o	Giá hiện tại
o	Giá trước đó
o	Phần trăm khuyến mãi
o	Số lượng sản phẩm đã bán
o	Lượt đánh giá, điểm đánh giá
o	Hãng
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chr_opt = Options()

def get_lazada_data(url):
    #Run Google Chrome:
    dri = webdriver.Chrome(options=chr_opt)

    #Access to url:
    obj = dri.get(url)

    #Get data from html tag and element
    title = dri.find_element(By.XPATH, "//h1[@class='pdp-mod-product-badge-title']").text
    product_price_now = dri.find_element(By.XPATH, "//span[@class='pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl']").text
    product_price_before = dri.find_element(By.XPATH, "//span[@class='pdp-price pdp-price_type_deleted pdp-price_color_lightgray pdp-price_size_xs']").text
    discount_percent = dri.find_element(By.XPATH, "//span[@class='pdp-product-price__discount']").text
    rating_quantity = dri.find_element(By.XPATH, "//a[@class='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-review-summary__link']").text
    rating = len(dri.find_elements(By.XPATH, "//img[@class='star']"))

    #Process data crawling:
    product_price_now = int(product_price_now.replace('.', '').replace('₫', ''))
    product_price_before = int(product_price_before.replace('.', '').replace('₫', ''))
    discount_percent = int(discount_percent.replace('%',''))
    rating_quantity = int(rating_quantity.split(' ')[0])


    return [title, product_price_now, product_price_before, discount_percent, rating_quantity, rating]

url = "https://www.lazada.vn/products/apple-iphone-15-pro-max-256gb-chinh-hang-vna-i2416996609-s11886272997.html"

data = get_lazada_data(url)
print(data)

