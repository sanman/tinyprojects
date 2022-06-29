from currency_converter_with_rate import currency

converter = currency.Currency()

base_currency = input("Enter the base currency: ")
target_currency = input("Enter the target currency: ")
data = converter.convert().base(base_currency).target(target_currency).amount(1).get()
                                
print(data)