import pdb
from datetime import date
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

# Delete all transactions
transaction_repository.delete_all()
# Delete all merchants
merchant_repository.delete_all()

# Inital merchants

# January
merchant_jan_1 = Merchant("Tesco")
merchant_jan_2 = Merchant("Boots")
merchant_jan_3 = Merchant("McDonalds")
merchant_repository.save(merchant_jan_1)
merchant_repository.save(merchant_jan_2)
merchant_repository.save(merchant_jan_3)

# February
merchant_feb_1 = Merchant("Asda")
merchant_feb_2 = Merchant("Blackfiars")
merchant_feb_3 = Merchant("The Merchant")
merchant_feb_4 = Merchant("Dominos")
merchant_repository.save(merchant_feb_1)
merchant_repository.save(merchant_feb_2)
merchant_repository.save(merchant_feb_3)
merchant_repository.save(merchant_feb_4)

# March
merchant_mar_1 = Merchant("Roast")
merchant_mar_2 = Merchant("Sainsburys")
merchant_repository.save(merchant_mar_1)
merchant_repository.save(merchant_mar_2)

# April
merchant_apr_1 = Merchant("Tesco")
merchant_apr_2 = Merchant("John Lewis")
merchant_apr_3 = Merchant("Vans")
merchant_repository.save(merchant_apr_1)
merchant_repository.save(merchant_apr_2)
merchant_repository.save(merchant_apr_3)

# May
merchant_may_1 = Merchant("Kwikfit")
merchant_may_2 = Merchant("The Islay Inn")
merchant_may_3 = Merchant("Scotrail")
merchant_repository.save(merchant_may_1)
merchant_repository.save(merchant_may_2)
merchant_repository.save(merchant_may_3)

#June
merchant_june_1 = Merchant("Falafel To Go")
merchant_june_2 = Merchant("Tesco")
merchant_june_3 = Merchant("Halfords")
merchant_june_4 = Merchant("The Merchant")
merchant_june_5 = Merchant("Pizza Hut")
merchant_repository.save(merchant_june_1)
merchant_repository.save(merchant_june_2)
merchant_repository.save(merchant_june_3)
merchant_repository.save(merchant_june_4)
merchant_repository.save(merchant_june_5)

# Inital transactions

# January
transaction_6 = Transaction(15.25, merchant_jan_1, date(2023, 1, 10), "Groceries 🥖")
transaction_7 = Transaction(10.00, merchant_jan_2, date(2023, 1, 9), "Personal Care 💈")
transaction_8 = Transaction(5.00, merchant_jan_3, date(2023, 1, 7), "Eating Out 🍔")

# February
transaction_9 = Transaction(20.00, merchant_feb_1, date(2023, 2, 10), "Groceries 🥖")
transaction_10 = Transaction(32.00, merchant_feb_2, date(2023, 2, 9), "Pub 🍻")
transaction_11 = Transaction(15.40, merchant_feb_3, date(2023, 2, 7), "Pub 🍻")
transaction_12 = Transaction(10.00, merchant_feb_4, date(2023, 2, 7), "Eating Out 🍕")

# March
transaction_13 = Transaction(10.00, merchant_mar_1, date(2023, 3, 10), "Eating Out 🍕")
transaction_14 = Transaction(42.20, merchant_mar_2, date(2023, 3, 9), "Groceries 🥖")

# April
transaction_15 = Transaction(20.00, merchant_apr_1, date(2023, 4, 10), "Groceries 🥖")
transaction_16 = Transaction(50.00, merchant_apr_2, date(2023, 4, 9), "Shopping 🛍️")
transaction_17 = Transaction(60.00, merchant_apr_3, date(2023, 4, 7), "Clothes 👕")

# May
transaction_18 = Transaction(90.00, merchant_may_1, date(2023, 5, 10), "Autocare 🚗")
transaction_19 = Transaction(20.00, merchant_may_2, date(2023, 5, 9), "Pub 🍻")
transaction_20 = Transaction(10.00, merchant_may_3, date(2023, 5, 7), "Transport 🚆")

# June
transaction_1 = Transaction(04.50, merchant_june_1, date(2023, 6, 10), "Takeaway 🥡")
transaction_2 = Transaction(12.50, merchant_june_2, date(2023, 6, 9), "Groceries 🛒")
transaction_3 = Transaction(25.00, merchant_june_3, date(2023, 6,7), "Autocare 🚗")
transaction_4 = Transaction(15.00, merchant_june_4, date(2023, 6, 7), "Pub 🍻")
transaction_5 = Transaction(20.00, merchant_june_5, date(2023, 6, 5), "Eating Out 🍕")

# Save transactions to database
transaction_repository.save(transaction_1)
transaction_repository.save(transaction_2)
transaction_repository.save(transaction_3)
transaction_repository.save(transaction_4)
transaction_repository.save(transaction_5)
transaction_repository.save(transaction_6)
transaction_repository.save(transaction_7)
transaction_repository.save(transaction_8)
transaction_repository.save(transaction_9)
transaction_repository.save(transaction_10)
transaction_repository.save(transaction_11)
transaction_repository.save(transaction_12)
transaction_repository.save(transaction_13)
transaction_repository.save(transaction_14)
transaction_repository.save(transaction_15)
transaction_repository.save(transaction_16)
transaction_repository.save(transaction_17)
transaction_repository.save(transaction_18)
transaction_repository.save(transaction_19)
transaction_repository.save(transaction_20)

# merchants = merchant_repository.select_all()
# transactions = transaction_repository.select_all()
# print(transactions)