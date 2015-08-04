
optional_size = ["XSmall", "Small", "Medium", "Large", "XLarge", "XXLarge"]
optional_color = ["White", "Yellow", "Green", "Blue", "Red", "Brown", "Purple", "Gray", "Black"]

def str_to_bol(ans):
    ans=ans.lower()
    while ans not in ["y", "yes", "n", "no"]:    
        ans=raw_input("Please enter yes/no.  ")
    if ans in ["y", "yes"]:
        return True
    else: 
        return False
        
def str_to_float (ans):
    try:
        ans=float(ans)
    except Exception, e:
        #I get a message unused var e. Whats the difference between e and Exception?"
        print "Please type in a number"
        str_to_float(ans)
    return ans
        
def add_color_selection ():
    color_selection = []
    print "Color selection." 
    for color in optional_color:
        print (color + " - add to color selection?")
        answer=str_to_bol(raw_input("Please type yes or no."))
        if answer == True: 
            color_selection.append(color)
    if len(color_selection)==0:
        print "You must add at least one size to size selection."
        add_color_selection()
    return color_selection

def add_size_selection (name):
    size_selection = {}
    # What is the best way for user to choose optional size? best is yes or no. 
    print "Size selection." 
    for size in optional_size:
        print (size + " - add to Size selection?")
        answer=str_to_bol(raw_input("Please type yes or no."))
        if answer == True: 
            #User puts in a string, we transfer to a float. I thing better prevent exception than hanel exception.
            weight = str_to_float(raw_input("Weight of bicycle {0} size {1} :".format(name, size)))
            cost = str_to_float(raw_input("Cost of bicycle {0} size {1} :".format(name, size)))
            size_selection[size]=[weight, cost]
    if len(size_selection)==0:
        print "You must add at least one size to size selection."
        add_size_selection(name)
    return size_selection
    