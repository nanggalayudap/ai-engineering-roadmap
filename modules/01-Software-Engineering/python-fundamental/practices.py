item_list = {
    "A01":{
        "name": "Minyak Goreng",
        "price": 12000
    },
    "A02":{
        "name": "Beras 1Kg",
        "price": 21000
    },
    "A01":{
        "name": "Indomie",
        "price": 18000
    }
}

for kode, info in item_list.items():
    print(f"[{kode}] {info["name"]} {info["price"]:,}")
    