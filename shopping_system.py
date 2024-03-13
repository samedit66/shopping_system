import random


Money = int


class Product:
    _cost: int

    def __init__(self, name: str, cost: Money):
        self._name = name
        self._cost = cost

    def name(self) -> str:
        return self._name

    def cost(self) -> Money:
        return self._cost
    
    def __eq__(self, other: 'Product') -> bool:
        return (self.name() == other.name()) and (self.cost() == other.cost())

    def __repr__(self) -> str:
        return f'Product(name={self.name()}, cost={self.cost()})'


class Seller:
    _name: str

    def __init__(self, name: str):
        self._name = name

    def name(self):
        return self._name

    def _total_cost(self, products: list[Product]) -> Money:
        total = sum(product.cost() for product in products)
        return total

    def sell_products(self, products: list[Product], payment: Money) -> None:
        total_cost = self._total_cost(products)

        if total_cost > payment:
            raise RuntimeError('Not enough money to buy products')
        
        return total_cost - payment
    
    def __repr__(self):
        return f'Seller(name={self.name()})'


class Shop:
    _products: list[Product]
    _sellers: list[Seller]

    def __init__(self):
        self._products = [
            Product('Milk', 100),
            Product('Pepsi', 200),
            Product('Salad Politeh', 40),
        ]
        self._sellers = [
            Seller('Mary'),
            Seller('Bob'),
            Seller('Oleg')
        ]

    def buy_products(self, products: list[Product], payment: Money) -> None:
        return random.choice(self._sellers).sell_products(products, payment)

    def product_list(self) -> list[Product]:
        return self._products

    def seller_list(self) -> list[Seller]:
        return self._sellers

    def _extract_product(self, product: Product) -> None:
        self._products.remove(product)

    def _put_product(self, product: Product) -> None:
        self._products.remove(product)


class Wallet:
    _amount: Money

    def __init__(self, initial: Money = 0):
        self._amount = initial

    def money_amount(self) -> Money:
        return self._amount

    def withdraw_money(self, money: Money):
        self._amount -= money

    def put_money(self, money: Money):
        self._amount += money

    def __repr__(self) -> str:
        return f'Wallet(money_amount={self.money_amount})'


class Client:
    _wallet: Wallet
    _basket: list[Product]
    _shop: Shop

    def __init__(self, shop: Shop, initial_money: Money = 0):
        self._wallet = Wallet(initial_money)
        self._basket = []
        self._shop = shop

    def withdraw_money(self, money: Money):
        self._wallet.withdraw_money(money)

    def put_money(self, money: Money):
        self._wallet.put_money(money)

    def money_amount(self) -> Money:
        return self._wallet.money_amount()

    def put_in_basket(self, product: Product) -> None:
        self._shop._extract_product(product)
        self._basket.append(product)

    def put_out_basket(self, product: Product) -> None:
        self._shop._put_product(product)
        self._basket.remove(product)

    def basket(self) -> list[Product]:
        return self._basket