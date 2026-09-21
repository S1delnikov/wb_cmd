import argparse
from service.autochrome import parse_product_cards

parser = argparse.ArgumentParser(description='Данный скрипт автоматически открывает браузер Google Chrome \
                                 и считывает информацию по карточкам товаров на Wildberries. Полученные \
                                 данные сохраняются в файл.')
parser.add_argument('url_cards', type=str, help='Ссылка на результат поиска товаров')
parser.add_argument('outfile', type=str, help='Файл, в который нужно сохранить результат')
args = parser.parse_args()

print("=============================")
print("========Начало запроса=======")
print("=============================")

if parse_product_cards(args.url_cards, args.outfile):
    print('\n')
    print("=============================")
    print("===Запрос выполнен успешно===")
    print("=============================")