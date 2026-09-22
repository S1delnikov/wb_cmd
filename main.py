import sys
import argparse
from service.autochrome import parse_product_cards
from service.file import check_file_type

parser = argparse.ArgumentParser(description='Данный скрипт автоматически открывает браузер Google Chrome \
                                 и считывает информацию по карточкам товаров на Wildberries. Полученные \
                                 данные сохраняются в файл.')
parser.add_argument('url_cards', type=str, help='Ссылка на результат поиска товаров')
parser.add_argument('outfile', type=str, help='Файл, в который нужно сохранить результат')
args = parser.parse_args()

file_type = check_file_type(args.outfile)

if file_type == False:
    sys.exit(1)
else:
    parse_product_cards(args.url_cards, args.outfile, file_type)
    sys.exit(0)
    