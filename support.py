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
        # Whats the difference between e and Exception?"
        while True: 
            ans= raw_input("Please type in a number:    ")
            try:
                ans=float(ans)
                break
            except Exception, e:
                pass
    return ans

def str_to_positive_int (ans): 
    while True: 
        try:
            ans=int(ans)
        except Exception, e:
            # Mentor - Whats the difference between e and Exception?"
            while True: 
                ans= raw_input("Please type a non negative number:    ")
                try:
                    ans=int(ans)
                    break
                except Exception, e:
                    pass
        if ans<0:
            print "Please type a non negative number."
        else:
            break
    return ans

"""
catagories = ["Mountain", "City", "HighWay"]
optional_sizes = ["XSmall", "Small", "Medium", "Large", "XLarge", "XXLarge"]
optional_colors = ["White", "Yellow", "Green", "Blue", "Red", "Brown", "Purple", "Gray", "Black"]
"""

def choose_1_from_list (name_of_list, lst): 
    print " ", name_of_list
    for i in range(0,len(lst)):
        print "   ", i+1, " - ", lst[i]
    ans = str_to_positive_int(raw_input("  Choose one option by number:     "))
    return lst[ans-1]



def choose_selection_from_list (name_of_list, lst): 
    lst_to_return = []
    index_lst = [] 
    # For convenience we will build list of indexs, and convert list of values at the end. 
    # There is a difference between the list indexes which are from 0 and the index for user which is from 1. 
    # We will use list index, and will convert to user index before output and after input. 
    print " ", name_of_list
    for i in range(0,len(lst)):
        print "   ", i+1, " - ", lst[i]
    index_lst.append(str_to_positive_int(raw_input("Choose an option by number:     "))-1)
    while len(index_lst)<len(lst): # The while ends when user types 0 (index=-1) or when all options are chosen.  
        print name_of_list
        for i in range(0,len(lst)):
            if i not in index_lst: 
                print "  ", i+1, " - ", lst[i]
            else: 
                print "  ", i+1, " - ", lst[i], "(Choosen)"
        index = str_to_positive_int(raw_input("  Add an option by number, or 0 to continue:     "))-1
        if index == -1: 
            break
        if index >= len(lst) or index<-1: # 5 options. user enters 6 its an error. it will show as index=5. so if index>=len(lst) we have a problem. 
            print "  Please choose a valid option."
        if index in index_lst:
            print "  Please choose a new option." 
        else: 
            index_lst.append(index)
    index_lst.sort()
    for i in index_lst:
        lst_to_return.append(lst[i])
    return lst_to_return

def add_model_name (): 
    name = raw_input ("  Model name:  ")
    while name == "":
        print "  Model name must have at least 1 character" 
        name = raw_input ("  Model name:  ")
    return name

"""
def add_catagory (): 
    return choose_1_from_list("Catagories", catagories)
    
    print "Catagories:  "
    for catagory in catagories: 
        print catagory, "     ",  
    ans= raw_input("m/c/h   ").lower
    while ans not in ["m", "c", "h"]:    
        ans=raw_input("Please enter m/c/h  ")
    if ans == "m": 
        return "Mountain"
    elif ans == "c": 
        return "City"
    else: 
        return "HighWay" 
        
        
def add_color_selection ():
    return choose_selection_from_list("Color Selection", optional_colors)
    
    color_selection = []
    print "Color selection." 
    for color in optional_color:
        print (color + " - add to color selection?")
        answer=str_to_bol(raw_input("Please type yes or no."))
        if answer == True: 
            color_selection.append(color)
    if len(color_selection)==0:
        print "You must add at least one color to color selection."
        add_color_selection()
    return color_selection
    """

def add_size_info (model_name, optional_sizes):
    size_info={} # Dictionary to return in the end of function. The structure --> {size:[weight, cost],  ...} 
    size_selection = choose_selection_from_list("Size Selection", optional_sizes) # Size selection for the specific model. 
    for size in size_selection: 
        info=[] 
        print model_name, size
        info.append(str_to_float(raw_input("Enter weight:    ")))
        info.append(str_to_float(raw_input("Enter cost:  ")))
        size_info[size]=info
    print size_info
    return size_info    

    """
    size_selection = {}
    # What is the best way for user to choose optional size? best is yes or no. 
    print "Size selection." 
    for size in optional_size:
        print (size + " - add to Size selection?")
        answer=str_to_bol(raw_input("Please type yes or no."))
        if answer == True: 
            #User puts in a string, we transfer to a float. I thing better prevent exception than hanel exception.
            weight = str_to_float(raw_input("Weight of bicycle {0} size {1}:    ".format(name, size)))
            cost = str_to_float(raw_input("Cost of bicycle {0} size {1}:    ".format(name, size)))
            size_selection[size]=[weight, cost]
    if len(size_selection)==0:
        print "You must add at least one size to size selection."
        add_size_selection(name)
    return size_selection
    """
    
def choose_size (model, size_dic): 
    print "  Selection of Sizes for model", model, ":"
    for size in size_dic: 
        print size, "     ", "Weight:", size_dic[size][0], "Cost:", size_dic[size][1]
    choice = raw_input("Type Model Name:     ")
    while not(size_dic.__contains__(choice)): # choice not in size_dic: 
        print "Please type valid Model from list."
        choice = raw_input("Type Model Name:     ")
    return choice