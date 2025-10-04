def add_sprinkless(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkless
@add_fudge
def get_ice_cream(flaver):
    print(f"Here is your {flaver} ice cream")

get_ice_cream("vanilla")