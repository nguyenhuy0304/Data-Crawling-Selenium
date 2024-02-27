""" Tên Sản Phẩm
 Giá Bán
 Lượt Bán
 Địa Chỉ Vận Chuyển
 Tỷ Lệ Giảm Giá
 Lượt Đánh Giá 5 Sao
 Phân Loại

==> Ghi ra thành 1 file Excel !!!
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import Workbook

#Cấu hình, chọn trình duyệt web Chrome:
chr_opt = Options()

#Tạo kết nối với url và trích xuất dữ liệu thành 1 list
def get_laz_data(url):
    try:

        #Run Google Chrome
        dri = webdriver.Chrome(options=chr_opt)

        #Access to url
        obj = dri.get(url)

        #Get data from html tag & element
        # data = dri.find_element(By.XPATH, "//div[@class='styles__BodyContainerStyled-sc-w4gwmz-0 coqMVo']").text
        product_title = dri.find_element(By.XPATH, "//div[@class='pdp-mod-product-badge-wrapper']").text
        product_price = dri.find_element(By.XPATH, "//span[@class='pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl']").text
        product_discount = dri.find_element(By.XPATH, "//span[@class='pdp-product-price__discount']").text
        # product_category = dri.find_element(By.XPATH, "//a[@title='Smartphones']").text

        return {'Product Title': product_title, 'Product Price': product_price, 'Product Discount': product_discount}

    except Exception as e:
        print(e)

#Đọc file và lấy đường dẫn url từ file:
def get_urls(file_path, file_name):
    try:
        urls = list()
        #Open file
        # file = open(file_path)

        with open(file_path + file_name) as file:
            f = file.read()
            # urls.append(f)
            urls = f.split('\n')
        return urls

    except Exception as e:
        print(e)

#Ghi dữ liệu vào file Excel:
def write_to_excel(file_name, data):
    # Tạo một Workbook mới
    wb = Workbook()

    # Chọn Sheet đầu tiên (mặc định)
    ws = wb.active

    # Thêm dữ liệu vào các ô trong Sheet
    for row in data:
        ws.append(row)

    # Lưu Workbook vào tệp Excel
    wb.save(file_name)

#Đọc file và lấy ra các urls có trong file:
path = './'
f_name = 'laz_urls.txt'
urls = get_urls(path, f_name)
print(urls)

#Trích xuất dữ liệu từ các urls:
products = list()
for url in urls:
    products.append(get_laz_data(url))

#Khởi tạo sheet trong workbook:
wb = Workbook()
sheet = wb.active

#Biến đổi list trước khi ghi vào file Excel:
head_sheet_list = list()
value_sheet_list = list()
list_data_sraping_lazada = list()

for i in products:
    for k, v in i.items():
        head_sheet_list.append(k)
        value_sheet_list.append(v)

list_data_sraping_lazada.append(head_sheet_list)
list_data_sraping_lazada.append(value_sheet_list)

# Gọi hàm để ghi dữ liệu vào tệp Excel
write_to_excel('Data Scraping from Python.xlsx', list_data_sraping_lazada)