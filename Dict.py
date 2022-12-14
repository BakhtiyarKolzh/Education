# dict

########################################################################################################################
"""

d={
    "table": "стол",
    "computer": "компьютер",
    "chair": "кресло"
}

print(d["table"])

# if "chair" in d:
#     print(d["chair"])

"""
########################################################################################################################
"""
items = [{"t": "T"},{"one": 1, "two": 2},4]
print(items)
"""
########################################################################################################################
#Skidka
"""
import json
f=open("items.json")
items=json.load(f)

for item in items:
    if "discount" in item:
        print(item)
        saving=item["price"]*item["discount"]
        print(f"You can save ${saving}!Yeah!")
        
"""
########################################################################################################################

import json

# Перебор в цикле
# def quantity(items: list[dict], name: str)-> int:
#     for item in items:
#         if item["name"]==name:
#             return item["quantity"]
#     return 0
# Перебор в цикле с суммированием
def items_quantity(items: list[dict], name: str)-> int:
    s=0
    for item in items:
        if item["name"]==name:
            s+= item["quantity"]
    return s

f=open("items.json")
items=json.load(f)


# print(items_quantity(items, "Keyboard"))
#####################################

def items_buy(items: list[dict], name: str, quantity: int )->float:
    if quantity>items_quantity(items, name):
        print(f"Not enough {name}s")
        return 0

    amount=0
    for item in items:
        if item["name"]==name:
            available=min(item["quantity"],quantity)
            to_pay=item["price"]*available

            if "discount" in item:
                to_pay -= item["price"] * available * item["discount"]
            amount+=to_pay
            item["quantity"]-=available
            quantity-=available

    return amount



f=open("items.json")
items=json.load(f)
for item in items:
    if "discount" not in item:
        item["discount"]=0
items.sort(key=lambda x: x["price"] - x["price"]*x["discount"])

print(items_buy(items, "Monitor", 15))
print(items)
for item in items:
    if item["name"]=="Monitor":
        print(item)

# print(items_buy(items, "Keyboard", 7))
# print(items)


########################################################################################################################


