from support import choose_one_from_list

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

    def log(self):
        s = "\nMODEL NAME: {}\t CATEGORY: {}\t DESCRIPTION: {}"
        print s.format(self.name, self.category, self.description)
        print "COLOR SELECTION: \t",
        for color in self.colors:
            print color, "\t",
        print ""
        for size, details in self.sizes.iteritems():
            s = "SIZE: {}\t WEIGHT: {} Kg\t COST: {} US$"
            print s.format(size, details['weight'], details['price'])


def make_model (): 
    model_name = add_model_name()
    catagory = choose_1_from_list("Catagories", CATEGORIES) 
    description = raw_input ("Description:\t")
    print "Add color to color selection." 
    color_selection = choose_selection_from_list ("Color Options", COLORS)
    size_info = add_size_info(model_name, SIZES) # This includes size selection, and additional info for each size. 
    models[model_name]=[catagory, description, color_selection, size_info]

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

# The type of bike is determined by: model, size and color. 
# Each bike should have a unique Serial. 
# bicycles = {serial: [model, color, size]  ...} actually better: 
# bicycles = [[model, color, sizes],  ...]     since the serial are from 0 onwards, the serial is the place of bike in bicycles. 

bicycles = []
count = 0
class Bicycle ():
    def __init__ (self, model, color, size, count):
        self.serial = count
        count+=1
        bicycles.append([model, color, size])

def make_bicycles ():
    #First we choose model, than size and color than quantity. Than we create bicycles by the constructor. 
    #Mentor - I would like to use the support file. but than I will have to send it the models dic, instead of simply using this dic. is there a solution?
    print "Choose a model from list of models:"
    print_models()   
    choosen_model=raw_input("\nType Model Name:   ")
    while not(models.__contains__(choosen_model)): 
        print "Model not recognized. Please type Name of Model from list of models."
        choosen_model = raw_input("\nType Model Name:     ")
    print "Choose color from selection of colors for model", choosen_model, ":"
    color = choose_1_from_list("Selection of colors", models[choosen_model][2])
    size = choose_size(choosen_model, models[choosen_model][3])
    print "How many Bicycles to manufacture of \tMODEL: \t{} \t COLOR: \t{} \tSIZE: \t{} \t?" .format (choosen_model, color, size)
    quantity = str_to_positive_int(raw_input("Type Quantity\t"))
    while quantity > 10000: 
        print "You can only produce up to 10,000 units at a time."
        quantity = str_to_positive_int(raw_input("Type Quantity:     "))
    for i in range(quantity):        
        Bicycle(choosen_model, color, size, count)

def print_intro():
    print "\nWelcome to Bicycle Industry model."
    print "\nLets start with creating bicycle models." 

def main(): 
    print_intro()

    choice = choose_one_from_list(["Let's create some models!",
                                   "Use sample model library"])
    if choice == 0:
        models = make_models()
    elif choice == 1:
        models = sample_model_library()

    for name, model in models.iteritems():
        model.log()

    """

    print "Choose option from list:"
    print "\t1 - Lets create some models ! "
    print "\t2 - Use sample model liberary. "
    index0=str_to_int(raw_input("Choose an option by number:     "))
    while not(index0==1 or index0==2): # Accepting only 1 or 2. 
        index0=str_to_int(raw_input("Please type 1 or 2:\t"))
    if index0==1:
        i=1
        while True: 
            print "\nMODEL NUMBER" , i ,":"
            i+=1
            make_model()
            ans=str_to_bol(raw_input("Would you like to add another model?  yes/no  "))
            if ans == False: 
                break
    else:
        sample_model_liberary()
    print models
    # Mentor - for sample model liberary. I print models in the end of sample_model_liberary function 
    # and after the function. After the function the models dict is empty. 
    # models is defined out of a function, and therefor, as far as I understand is a global var. Can't I change
    # the value from within a function? 
    
    print "\nLets create some bicycles"
    while True: 
        make_bicycles()
        ans=str_to_bol(raw_input("\nWould you like to add another model?  yes/no  "))
        if ans == False: 
            break 
    print bicycles
    
    print "\nLets open some shops" 
    """

if __name__ == "__main__":
    main()
