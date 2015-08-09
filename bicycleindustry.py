from support import *

catagories = ["Mountain", "City", "HighWay"]
optional_sizes = ["XSmall", "Small", "Medium", "Large", "XLarge", "XXLarge"]
optional_colors = ["White", "Yellow", "Green", "Blue", "Red", "Brown", "Purple", "Gray", "Black"]

# Main database - 
# Main dictionary of Bicycle models. 
# For each model user will have to add additional info: category (road or mountain) and description, color selection and size selection. 
# For each size of model, user will ave to add additional info: weight and cost.
# models = {model_name: [catagory(str), description (str), color_selection[list], size_selection{size:[weight, cost])   ...}  ...} 
# Should I chose tuples or lists? 

models = {}
def make_model (): 
    model_name = add_model_name()
    catagory = choose_1_from_list("Catagories", catagories) 
    description = raw_input ("Description:\t")
    print "Add color to color selection." 
    color_selection = choose_selection_from_list ("Color Options", optional_colors)
    size_info = add_size_info(model_name, optional_sizes) # This includes size selection, and additional info for each size. 
    models[model_name]=[catagory, description, color_selection, size_info]

def sample_model_liberary ():
    models = {
        'H1': ['HighWay', 'Fine, Lights, Stable.', ['Blue', 'Red'], {'Small': [3.0, 1000.0], 'Large': [3.3, 1100.0]}], 
        'Mountain 100': ['Mountain', 'Good, Shock absorber. ', ['Brown', 'Black'], {'Large': [4.0, 1000.0], 'XXLarge': [4.4, 1100.0]}], 
        'M1': ['Mountain', 'Fine, Shock absorber.', ['Brown', 'Black'], {'Large': [4.0, 500.0], 'XXLarge': [4.4, 550.0]}], 
        'City 100': ['City', 'Good, Stable.', ['Yellow', 'Green'], {'XLarge': [3.3, 550.0], 'Medium': [3.0, 500.0]}], 
        'C1': ['City', 'Fine, Stable.', ['Yellow', 'Green'], {'XLarge': [3.3, 275.0], 'Medium': [3.0, 250.0]}], 
        'Highway 100': ['HighWay', 'Good, Lights, Stable. ', ['Blue', 'Red'], {'Small': [3.0, 2000.0], 'Large': [2.2, 2200.0]}]
        }
    print models

def print_models(): 
    for model in models: 
        print "\nMODEL NAME: {}\t CATAGORY: {}\t DESCRIPTION: {}".format(model, models[model][0], models[model][1])
        print "COLOR SELECTION: \t",
        for color in models[model][2]:
            print color, "\t",
        print 
        for size in models[model][3]:
            print "SIZE: {}\t WEIGHT: {} Kg\t COST: {} US$" .format(size, models[model][3][size][0], models[model][3][size][1])

"""
def print_model(model): 
    print "MODEL NAME: {}\t CATAGORY: {}\t DESCRIPTION: {}".format(model, models[model][0], models[model][1])
    print "COLOR SELECTION: \t",
    for color in models[model][2]:
        print color, "\t",
    print 
    for size in models[model][3]:
        print "SIZE: {}\t WEIGHT: {}\t COST: {}\t" .format(size, models[model][3][size][0], models[model][3][size][1])
"""

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

"""
print "Lets start with creating our main database." 
# Creating new models.  
While True: 
    model
    #Info for each type. 

# Each bike has a unique serial. 
# users can find type of bike by serial.
# Creating bikes
# user can create bike by type. 
# creating bike creates a bike with a unique ID. 

# Shops 
# Every shop will have inventory by serials, 


and users can own bikes by serials. 

function sellRequest (model, size, color):
    look for requested bike in inventory. if exist: 1)return to shop approval, and details of bike, 2) reduce bike from inventory. if not, return refusal and send inventory.

# Bicycle
count = 0
class Bicycle ():
    def __init__ (self, modelName, size, color):
        self.serial = count
        count ++ 
        # modelName, size and color can only be of a certain kind, mentioned in company's database.  
        if modelName in model dictionary: 
            self.modelName = modelName
        else: provide model list and request user to chose. 
        #same proceedure with size and color. 
        self.size = size
        self.color = color
        add entry to inventory
        
class Shop ():    
    sellMargin=0.2
    inventory = {serial:[model, size, color, weight, cost]    ......}
    def __init__ (self, name):
        self.name =name
    def buyBike (self, modelName, size, color):
        #We will request sell from company
        sellRequest(modelName, size, color)
        if approved add bike to inventory
        if not present to user companys inventory and allow user to choose a different bike. 
        call sellRequest fun again with the new requested bike. 
    profitPerModelDic = {model:profit .......}  
    function sellRequest (model, size, color):
    look for requested bike in inventory. if exist: 1)return to customer approval, and details of bike, 2) reduce bike from inventory, and update profit dictionary. if not, return refusal and send inventory.
        
    
class Customer ():
        def __init__ (self, name, fund):
        self.name = name
        self.fund = fund
        own = {}
        def buy (modelName, size, color):
            #We will request sell from shop
            shop.sellRequest (modelName, size, color)
            if not present to user shop's inventory and allow user to choose a different bike. 
            call sellRequest fun again with the new requested bike. 
"""        

def main (): 
    print "\nWelcome to Bicycle Industry model."
    
    print "\nLets start with creating bicycle models." 
    # Creating new models. 2 options: Building models, or using prepared model liberary 
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
main ()