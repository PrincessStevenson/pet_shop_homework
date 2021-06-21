# WRITE YOUR FUNCTIONS HERE

# def get_pet_shop_name(pet_shop):
#     return pet_shop["name"]

# def get_total_cash(total_cash):
#     return total_cash["admin"]["total_cash"]

# def add_or_remove_cash(add_to_totalcash):
#     # return add_to_totalcash((int["total_cash"]) + [10])
# # def add_or_remove_cash(add_to_totalcash, 10):
# # return add_to_totalcash + 10

# def add_or_remove_cash(add_to_totalcash, cash):
#     # cash = 10
#     add_to_totalcash = get_total_cash + cash
#     cash = 10
    
#     return add_or_remove_cash


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


# get_total_cash(self.cc_pet_shop) can just be copy pasted
# because we're defining the function and it needs to be exactly the same.
# def get_total_cash
# we don't need the self. part so that can get deleted
# cc can stay but unnecessary
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    # doesn't need return function 

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, count):
    pet_shop["admin"]["pets_sold"] += count

def get_stock_count(pet_shop):
    # pets = pet_shop("pets")
    # number_of_pets = len(pets)
    # return number_of_pets
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, search_breed):
    found_pets_by_breed = []
    for pet in pet_shop["pets"]:
        # first time it runs, pet equals first pet in list, which is Sir Percy
        if pet["breed"] == search_breed:
            found_pets_by_breed.append(pet)
    return found_pets_by_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    if pet != None:
        pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet and customer_can_afford_pet(customer, pet):
        remove_customer_cash(customer, pet["price"])
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)