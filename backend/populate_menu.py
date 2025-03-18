from app import db
from app.models import Food, Drink
from app import create_app

app = create_app()

menu_data = {
    "Food": [
        # Food items (Sandwich-related)
        {"name": "White Bread", "price": 10, "image": "white_bread.png", "type": "bread"},
        {"name": "Whole Wheat", "price": 10, "image": "whole_wheat.png", "type": "bread"},
        {"name": "Burger Bun", "price": 10, "image": "burger_bun.png", "type": "bread"},
        {"name": "Egg", "price": 10, "image": "egg.png", "type": "Filling"},
        {"name": "Lettuce", "price": 10, "image": "lettuce.png", "type": "Filling"},
        {"name": "Luncheon Meat", "price": 15, "image": "luncheon_meat.png", "type": "filling"},
        {"name": "Burger Patty", "price": 15, "image": "burger_patty.png", "type": "filling"},
        {"name": "Tomato Slices", "price": 5, "image": "tomato_slices.png", "type": "filling"},
        {"name": "Cheese Slices", "price": 10, "image": "cheese_slices.png", "type": "filling"},
        {"name": "Tuna Mayo", "price": 10, "image": "tuna_mayo.png", "type": "Spread"},
        {"name": "Chicken Mayo", "price": 15, "image": "chicken_mayo.png", "type": "spread"},
        {"name": "Ketchup Mayo", "price": 5, "image": "ketchup_mayo.png", "type": "spread"},
        {"name": "Cheese Spread", "price": 10, "image": "cheese_spread.png", "type": "spread"},
        {"name": "Chocolate Spread", "price": 15, "image": "chocolate_spread.png", "type": "spread"},
        {"name": "Peanut Butter", "price": 5, "image": "peanut_butter.png", "type": "spread"},
    ],
    "Drink": [
        # Drink items (Flavors)
        {"name": "Orange", "size": "small", "price": 20, "image": "orange.png", "type": "flavor"},
        {"name": "Orange", "size": "medium", "price": 30, "image": "orange.png", "type": "flavor"},
        {"name": "Orange", "size": "large", "price": 40, "image": "orange.png", "type": "flavor"},
        {"name": "Watermelon", "size": "small", "price": 25, "image": "watermelon.png", "type": "flavor"},
        {"name": "Watermelon", "size": "medium", "price": 35, "image": "watermelon.png", "type": "flavor"},
        {"name": "Watermelon", "size": "large", "price": 45, "image": "watermelon.png", "type": "flavor"},
        {"name": "Mango", "size": "small", "price": 40, "image": "mango.png", "type": "flavor"},
        {"name": "Mango", "size": "medium", "price": 50, "image": "mango.png", "type": "flavor"},
        {"name": "Mango", "size": "large", "price": 60, "image": "mango.png", "type": "flavor"},
        {"name": "Apple", "size": "small", "price": 20, "image": "apple.png", "type": "flavor"},
        {"name": "Apple", "size": "medium", "price": 30, "image": "apple.png", "type": "flavor"},
        {"name": "Apple", "size": "large", "price": 40, "image": "apple.png", "type": "flavor"},
        {"name": "Melon", "size": "small", "price": 35, "image": "melon.png", "type": "flavor"},
        {"name": "Melon", "size": "medium", "price": 45, "image": "melon.png", "type": "flavor"},
        {"name": "Melon", "size": "large", "price": 55, "image": "melon.png", "type": "flavor"},
        {"name": "Pomelo", "size": "small", "price": 30, "image": "pomelo.png", "type": "flavor"},
        {"name": "Pomelo", "size": "medium", "price": 40, "image": "pomelo.png", "type": "flavor"},
        {"name": "Pomelo", "size": "large", "price": 50, "image": "pomelo.png", "type": "flavor"},

        # Drink Add-ons
        {"name": "Popping Boba", "price": 15, "image": "popping_boba.png", "type": "add-on", "size": None},
        {"name": "Sliced Fruit", "price": 15, "image": "sliced_fruit.png", "type": "add-on", "size": None},
        {"name": "Sago", "price": 5, "image": "sago.png", "type": "add-on", "size": None},
        {"name": "Nata de Coco", "price": 10, "image": "nata_de_coco.png", "type": "add-on", "size": None},
        {"name": "Tapioca Pearls", "price": 10, "image": "tapioca_pearls.png", "type": "add-on", "size": None},
    ]
}


def add_food_and_drinks():
    # Add food items
    for food_data in menu_data["Food"]:
        food = Food.query.filter_by(name=food_data["name"]).first()
        if not food:
            food = Food(
                name=food_data["name"],
                price=food_data["price"],
                image=food_data["image"],
                type=food_data["type"].lower(),
                stock=50
            )
            db.session.add(food)
    
    # Add drink items (including add-ons)
    for drink_data in menu_data["Drink"]:
        drink = Drink.query.filter_by(name=drink_data["name"], size=drink_data.get("size")).first()
        if not drink:
            drink = Drink(
                name=drink_data["name"],
                price=drink_data["price"],
                size=drink_data.get("size"),  # Size is optional (None for add-ons)
                image=drink_data["image"],
                type=drink_data["type"].lower(),
                stock=50
            )
            db.session.add(drink)
    
    db.session.commit()


@app.route('/populate_menu')
def main():
    # Create the tables first if they don't exist
    db.create_all()

    # Add food and drink items (including add-ons)
    add_food_and_drinks()

    return "Menu data populated successfully!"


if __name__ == '__main__':
    app.run(debug=True)
