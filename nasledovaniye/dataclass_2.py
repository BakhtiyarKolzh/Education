# Inheritance   Наследование
from dataclasses import dataclass
from decimal import Decimal
from uuid import uuid4
from client import Client
from transaction import Transaction, CardTransaction, QRTransaction

john = Client.from_name("John")
bill = Client.from_name("Bill")

transaction1 = CardTransaction.new_transaction(
    client_source=john,
    client_target=bill,
    amount=Decimal("100"),
    card_number="45454545454545454",
)

transaction2 = QRTransaction.new_transaction(
    client_source=john,
    client_target=bill,
    amount=Decimal("100"),
    qr_number="dasdsadsa34324fdfds43f",
)

def save_to_database(transaction: Transaction):
    assert isinstance(transaction, Transaction)
    transaction.save_to_database()

save_to_database(transaction1)
save_to_database(transaction2)
# save_to_database(2)

