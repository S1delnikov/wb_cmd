from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import settings
import time


def parse_product_cards(url_cards, outfile):
    driver = settings.get_driver
    try:
        driver.get(fr'{url_cards}') 
        input()
        product_cards = driver.find_elements(By.CLASS_NAME, settings.div_card)
        count = 1
        f = open(f'{outfile}', 'w', encoding='utf-8')
        
        start_time = time.perf_counter()
        for pc in product_cards:
            product_name = pc.find_element(By.CLASS_NAME, settings.div_product_name)
            product_name = ' '.join([pn.strip() if pn != None else "Нет бренда" for pn in product_name.text.split('/')])
            product_price = pc.find_element(By.CSS_SELECTOR, settings.div_product_price)
            f.write(f"{count}. {product_name} => {product_price.text}\n")
            count += 1
            print(f"\r{time.perf_counter() - start_time} сек.", end="", flush=True) 
        input()
    except:
        print("Что-то пошло не так.")
    finally:
        driver.quit()
