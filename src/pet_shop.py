# WRITE YOUR FUNCTIONS HERE

# Question 1
def get_pet_shop_name(pet_shop):
    pet_shop_name = pet_shop["name"]
    return pet_shop_name

# Question 2
def get_total_cash(pet_shop):
    sum = pet_shop["admin"]["total_cash"]
    return sum

# Question 3 & 4
def add_or_remove_cash(pet_shop, amount_of_cash):
    pet_shop["admin"]["total_cash"] += amount_of_cash

# Question 5
def get_pets_sold(pet_shop):
    sold = pet_shop["admin"]["pets_sold"]
    return sold

# Question 6
def increase_pets_sold(pet_shop, amount_sold):
    pet_shop["admin"]["pets_sold"] += amount_sold

# Question 7
def get_stock_count(pet_shop):
    count = 0
    for pet in pet_shop["pets"]:
        count +=1
    return count

# Question 8 & 9
def get_pets_by_breed(pet_shop, breed_to_find):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_to_find:
            breed_list.append(pet)
    return breed_list

# Question 10 & 11
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            found_pet = pet["name"]
            return pet
        else:
            None

# Question 12
def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)
            increase_pets_sold(pet_shop, 1) #Line added for Optional Q4
          
# Question 13
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

# Question 14
def get_customer_cash(customer):
    cash = customer["cash"]
    return cash

# Question 15
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# Question 16
def get_customer_pet_count(customer):
    pet_count = len(customer["pets"])
    return pet_count

# Question 17
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

# --- OPTIONAL ---

# Question 1, 2 & 3
def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

# Question 4, 5 and 6
def check_pet_exists(pet_shop, pet_to_find):
    for pet in pet_shop["pets"]:
        if pet == pet_to_find:
            return True
        else:
            return False
    

def sell_pet_to_customer(pet_shop, pet, customer):
    if customer_can_afford_pet(customer, pet) == True and check_pet_exists(pet_shop, pet) == True:
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        add_pet_to_customer(customer, pet)
        remove_pet_by_name(pet_shop, pet["name"])    
    else:
        return False


        