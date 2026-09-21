from seleniumbase import Driver

div_card = 'product-card__wrapper' # карточка товара
div_product_name = 'productLabelWrap--fzSqm' # блок с именем товара и его бренда из карточки товара
div_product_price = '[data-testid="product-card-current-price"]' # блок с ценой из карточки товара

get_driver = Driver(uc=True) # необнаруживаемый режим
