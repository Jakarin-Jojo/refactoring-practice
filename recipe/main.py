from recipe import Recipe


# replace redundant coed with a creating
def create_recipe(name, chocolate=0, coffee=0, sugar=0, milk=0, price=0.0):
    recipe = Recipe(name)
    recipe.chocolate = chocolate
    recipe.coffee = coffee
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = float(price)
    return recipe


if __name__ == '__main__':
    recipe1 = create_recipe("Coffee with sugar", 4, 2, 0, price=30.0)
    print(recipe1)

    recipe2 = create_recipe("Latte", 3, 2, 1, price=40.0)
    print(recipe2)

    recipe3 = create_recipe("Hot Chocolate", 0, 3, 2, 4, 30.0)
    print(recipe3)
