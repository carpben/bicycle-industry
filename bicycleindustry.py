from support import choose_yes_no, choose_one_from_list, choose_many_from_list
from support import text_input, positive_int_input

CATEGORIES = ["Mountain", "City", "HighWay"]
SIZES = ["XSmall", "Small", "Medium", "Large", "XLarge", "XXLarge"]
COLORS = ["White", "Yellow", "Green", "Blue", "Red", "Brown", "Purple", "Gray", "Black"]

class Model(object):
    def __init__(self, name, category, description, colors, sizes):
        self.name = name
        self.category = category
        self.description = description
        self.colors = colors
        self.sizes = sizes

    def __str__(self):
        model = "MODEL NAME: {}\t CATEGORY: {}\t DESCRIPTION: {}"
        model = model.format(self.name, self.category, self.description)


        colors = "COLOR SELECTION: \t"
        for color in self.colors:
            colors += "{}\t".format(color)

        sizes = ""
        for size, details in self.sizes.iteritems():
            s = "SIZE: {}\t WEIGHT: {} Kg\t COST: {} US$\n"
            sizes += s.format(size, details['weight'], details['price'])
        return "{}\n{}\n{}\n".format(model, colors, sizes)

def make_models():
    models = {}
    another = True
    while another:
        model = make_model()
        models[model.name] = model
        print("Would you like to add another model?")
        another = choose_yes_no()
    return models

def make_model():
    name = text_input("Model name: ")

    print "Choose a category:"
    _, category = choose_one_from_list(CATEGORIES)

    description = text_input("Description: ", True)

    print "Add color options:"
    colors = choose_many_from_list(COLORS)
    colors = [x for _, x in colors]

    print "Add size options:"
    # This includes size selection, and additional info for each size
    sizes = choose_many_from_list(SIZES)
    sizes = {x: {} for _, x in sizes}

    for size, details in sizes.iteritems():
        print "\nMODEL:\t{}\tSIZE:\t{}".format(name, size)
        details['weight'] = positive_int_input("Enter weight (Kg): ")
        details['price'] = positive_int_input("Enter cost (US $): ")

    return Model(name, category, description, colors, sizes)

def sample_model_library ():
    models = {}
    models['H1'] = Model(
        'H1',
        'HighWay',
        'Fine, Lights, Stable.',
        ['Blue', 'Red'],
        {
            'Small': {
                'weight': 3.0,
                'price': 1000.0
            },
            'Large': {
                'weight': 3.3,
                'price': 1100.0
            }
        }
    )

    models['Mountain 100'] = Model(
        'Mountain 100',
        'Mountain',
        'Good, Shock absorber.',
        ['Brown', 'Black'],
        {
            'Large': {
                'weight': 4.0,
                'price': 1000.0
            },
            'XXLarge': {
                'weight': 4.4,
                'price': 1100.0
            }
        }
    )

    models['M1'] = Model(
        'M1',
        'Mountain',
        'Fine, Shock absorber.',
        ['Brown', 'Black'],
        {
            'Large': {'weight': 4.0, 'price': 500.0},
            'XXLarge': {'weight': 4.4, 'price': 550.0}
        }
    )

    models['City 100'] = Model(
        'City 100',
        'City',
        'Good, Stable.',
        ['Yellow', 'Green'],
        {
            'XLarge': {'weight': 3.3, 'price': 550.0},
            'Medium': {'weight': 3.0, 'price': 500.0}
        }
    )

    models['C1'] = Model(
        'C1',
        'City',
        'Fine, Stable.',
        ['Yellow', 'Green'],
        {
            'XLarge': {'weight': 3.3, 'price': 275.0},
            'Medium': {'weight': 3.0, 'price': 250.0}
        }
    )

    models['Highway 100'] = Model(
        'Highway 100',
        'HighWay',
        'Good, Lights, Stable.',
        ['Blue', 'Red'],
        {
            'Small': {'weight': 3.0, 'price': 2000.0},
            'Large': {'weight': 3.3, 'price': 2200.0}
        }
    )
    return models

class Bicycle(object):
    def __init__ (self, model, color, size):
        self.model = model
        self.color = color
        self.size = size

    def __str__(self):
        s = "MODEL:{}\t COLOR:{}\t SIZE:{}"
        return s.format(self.model, self.color, self.size)

def make_bicycles(models):
    bicycles = []
    another = True
    while another:
        order = make_bicycle(models)
        bicycles.extend(order)
        print("Would you like to add another order of bicycles?")
        another = choose_yes_no()
    return bicycles

def make_bicycle(models):
    print "Choose a model from list of models: "
    names = map(lambda model: model.name, models.itervalues())
    _, name = choose_one_from_list(names)

    print "Choose color from selection of colors for model", name, ":"
    _, color = choose_one_from_list(models[name].colors)

    _, size = choose_one_from_list(models[name].sizes.keys())

    s = "How many Bicycles to manufacture of\t"
    s += "MODEL: \t{} \t COLOR: \t{} \tSIZE: \t{}?"
    print s.format(name, color, size)

    quantity = positive_int_input("Type Quantity: ")

    bicycles = []
    for i in range(quantity):
        bicycles.append(Bicycle(name, color, size))
    return bicycles

def main(): 
    print "\nWelcome to Bicycle Industry model."
    print "\nLets start with creating bicycle models." 

    choice, _ = choose_one_from_list(["Let's create some models!",
                                      "Use sample model library"])
    if choice == 0:
        models = make_models()
    elif choice == 1:
        models = sample_model_library()

    for name, model in models.iteritems():
        print model

    print "\nLets create some bicycles"

    bicycles = make_bicycles(models)
    for bicycle in bicycles:
        print(bicycle)

    print "\nLets open some shops" 

if __name__ == "__main__":
    main()
