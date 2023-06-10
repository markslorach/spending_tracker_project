import pdb
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

# delete all merchants
merchant_repository.delete_all()

# Inital merchants
merchant_1 = Merchant("Falafel To Go")
merchant_2 = Merchant("Tesco")
merchant_3 = Merchant("Halfords")
merchant_4 = Merchant("The Merchant")
merchant_5 = Merchant("MacTassos")

# Save merchants to database
merchant_repository.save(merchant_1)
merchant_repository.save(merchant_2)
merchant_repository.save(merchant_3)
merchant_repository.save(merchant_4)
merchant_repository.save(merchant_5)


# merchants = merchant_repository.select_all()
# print(merchants)