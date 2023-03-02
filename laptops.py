from selenium import webdriver

f = open('laptopsResults.txt', 'w')

url = 'https://altex.ro/laptopuri/cpl/filtru/price/3000-4000/'

driver = webdriver.Chrome()
driver.get(url)



initialCheck = 1

while(1):

    if (initialCheck != 1):
        
        button_xpath = '//*[@id="__next"]/div[2]/main/div[2]/div[1]/div[2]/div[4]/div/div/div/div[2]/a'
        button = driver.find_element_by_xpath(button_xpath).get_attribute('href')
                                
        if (str(button) == 'None'):
            break

        driver = webdriver.Chrome()
        driver.get(str(button))    

    products = driver.find_elements_by_class_name('Products-item')

    i = 1

    for product in products:
    
        title_xpath = '//*[@id="__next"]/div[2]/main/div[2]/div[1]/div[2]/ul/li[' + str(i) + ']/div/div[2]/div[1]/h2/a'
        title = product.find_element_by_xpath(title_xpath).text
    
        price_xpath = '//*[@id="__next"]/div[2]/main/div[2]/div[1]/div[2]/ul/li[' + str(i) + ']/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/span[1]'
        price = product.find_element_by_xpath(price_xpath).text

        link_xpath = '//*[@id="__next"]/div[2]/main/div[2]/div[1]/div[2]/ul/li[' + str(i) + ']/div/div[1]/a'
        link = product.find_element_by_xpath(link_xpath).get_attribute('href')

        print('No: ', i, file = f)
        print('Title: ', title, file = f)
        print('Price: ', price, file = f)
        print('Link: ', link, file = f)
        print('\n', file = f)
        
        i = i + 1
    
    driver.find_element_by_class_name('Toolbar-next')
    print('Next Page\n', file = f)
    initialCheck = 0

driver.close()
