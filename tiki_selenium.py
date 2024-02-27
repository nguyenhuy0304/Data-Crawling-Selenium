import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chr_opt = Options()

def get_tiki_data(url):
    # path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # ser = Service(path)

    #Run Google Chrome
    dri = webdriver.Chrome(options=chr_opt)

    #Access to url
    obj = dri.get(url)
    # time.sleep(5)

    #Get data from html tag & element
    # data = dri.find_element(By.XPATH, "//div[@class='styles__BodyContainerStyled-sc-w4gwmz-0 coqMVo']").text
    title = dri.find_element(By.XPATH, "//h1[@class='Title__TitledStyled-sc-1kxsq5b-0 cvyKhs']").text
    price = dri.find_element(By.XPATH, "//div[@class='product-price__current-price']").text
    quantity = dri.find_element(By.XPATH, "//div[@class='styles__StyledQuantitySold-sc-1swui9f-3 bExXAB']").text
    five_star_rating = dri.find_element(By.XPATH, "//div[@class='review-rating__level']//div[@class='review-rating__number']").text

    # #Process data crawling
    # price = int(price.replace('.', '').replace('₫', ''))
    # quantity = int((quantity.split(' '))[2])

    return {'Product Name': title, 'Product Price': price, 'Product quantity': quantity, '5 star': five_star_rating}

#Read file and get list url in file:
def get_urls(file_path, file_name):
    try:
        urls = list()
        #Open file
        # file = open(file_path)

        with open(file_path + file_name) as file:
            f = file.read()
            urls = f.split('\n')
        return urls

    except Exception as e:
        print(e)

# url = 'https://tiki.vn/lanh-dao-la-ngon-ngu-leadership-is-language-p273046888.html'

# data = get_tiki_data(url)
# print(data, type(data))

#Read file and get urls:
path = './'
f_name = 'tiki_urls.txt'
urls = get_urls(path, f_name)
print(urls)

#Scraping data from urls:
products = list()
for url in urls:
    products.append(get_tiki_data(url))

print(products)