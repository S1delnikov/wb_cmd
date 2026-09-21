from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumbase import Driver
import time

def parse_product_cards(url_cards, outfile):
    driver = Driver(uc=True) # необнаруживаемый режим

    try:
        driver.get(fr'{url_cards}') # кроссовки мужские
        input()
        product_cards = driver.find_elements(By.CLASS_NAME, 'product-card__wrapper')
        count = 1
        f = open(f'{outfile}', 'w', encoding='utf-8')
        print("=============================")
        print("========Начало запроса=======")
        print("=============================")
        start_time = time.perf_counter()
        for pc in product_cards:
            product_name = pc.find_element(By.CLASS_NAME, 'productLabelWrap--fzSqm')
            product_name = ' '.join([pn.strip() if pn != None else "Нет бренда" for pn in product_name.text.split('/')])
            product_price = pc.find_element(By.CSS_SELECTOR, '[data-testid="product-card-current-price"]')
            f.write(f"{count}. {product_name} => {product_price.text}\n")
            count += 1
            print(f"\r{time.perf_counter() - start_time} сек.", end="", flush=True)
        print('\n')
        print("=============================")
        print("===Запрос выполнен успешно===")
        print("=============================")
        input()
    except:
        print("Что-то пошло не так.")
    finally:
        driver.quit()