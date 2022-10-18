def dog():
    print("woof")


def cat():
    print("meow")


def pig():
    print("oink")


def cow():
    print("moo")


def duck():
    print("quack")


def horse():
    print("neigh")


def not_there():
    print("Sorry that key value pair doesn't exist")


animal_sounds = {"dog": dog, "cat": cat, "pig": pig, "cow": cow, "duck": duck, "horse": horse}


def get_input():
    player_input = input("Please enter an animal: ")
    player_input = player_input.lower().strip()
    animal_code = animal_sounds.get(player_input, not_there)
    return animal_code #ex return dog -- name  of fxn. not calling it

get_animal = get_input() #calling get_input and assigning value to get_animal. get_animal = dog

def speak():
    get_animal() #get_animal-- calling the fxn assigned to get_input. dog(). calls fxn

speak()
# was previously CALLING the function when making the dic 'dog':dog(), RETURN value from the func is stored



