def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]

def get_products(kw):
    products = [{
        "id": 1,
        "name": "iPhone 15 Pro Max",
        "price": 35000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/299033/iphone-15-pro-black-thumbnew-600x600.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iphone 15 Pro",
        "price": 28000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/299033/iphone-15-pro-black-thumbnew-600x600.jpg",
        "category_id": 1
    } , {
        "id": 3,
        "name": "iphone 15 Plus",
        "price": 25000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/303891/iphone-15-plus-128gb-xanh-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 4,
        "name": "iphone 15",
        "price": 22000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/281570/iphone-15-den-thumb-600x600.jpg",
        "category_id": 1
    }, {
        "id": 5,
        "name": "Samsung Galaxy Z Fold5 5G 1TB",
        "price": 48000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/310805/samsung-galaxy-z-fold5-%20xanh-600x600.jpg",
        "category_id": 1
    }, {
        "id": 6,
        "name": "Samsung Galaxy Z Fold4 5G 512GB",
        "price": 27000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/285031/samsung-galaxy-z-fold4-xanh-512gb-600x600.jpg",
        "category_id": 1
    } , {
        "id": 7,
        "name": "Samsung Galaxy S23 Ultra 5G 256GB",
        "price": 22000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/249948/samsung-galaxy-s23-ultra-thumb-xanh-600x600.jpg",
        "category_id": 1
    }, {
        "id": 8,
        "name": "Samsung Galaxy S23+ 5G 512GB",
        "price": 20000000,
        "image": "https://cdn.tgdd.vn/Products/Images/42/301798/samsung-galaxy-s23-plus-2-600x600.jpg",
        "category_id": 1
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products