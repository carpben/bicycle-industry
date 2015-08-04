import additional.py

print "Welcome to Bicycle Industry model. We will try to model the Bicycle industry."

# Main database - 
# Main dictionary of Bicycle models. 
# For each model user will have to add additional info: category (road or mountain) and description, color selection and size selection. 
# For each size of model, user will ave to add additional info: weight and cost.
# models = {model_name: [catagory(str), description (str), color_selection[list], size_selection{size:[weight, cost])   ...}  ...} 
# Should I chose tuples or lists? 

models = {}
def add_model (): 
    name = raw_input ("Type model name: ")
    catagory = raw_input ("Catagory:    ")
    description = raw_input ("Description:  ")
    color_selection = add_color_selection ()
    size_selection = add_size_selection (name)
    models[name]=[catagory, description, color_selection, size_selection]

print "Lets start with creating our main database." 
# Creating new models.  
i=1
while True: 
    print "model number" , i ,":"
    add_model()
    print "Would you like to add another model?" 
    ans=str_to_bol(raw_input("yes/no"))
    if ans == False: 
        break 

"""
# The type of bike is determined by: model, size and color. 
# Each bike should have a unique Serial. 
# bicycles = {serial: [model, color, size]  ...}

bicycles = {}
count = 0
class Bicycle ():
    def __init__ (self, model, color, size):
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