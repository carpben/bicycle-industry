def str_to_bool(ans):
    ans=ans.lower()
    if ans not in ["y", "yes", "n", "no"]:
        raise ValueError("Value should be one of y, yes, n or no")
    return ans in ["y", "yes"]

def text_input(question, allow_empty=False):
    while True:
        value = raw_input(question)

        if allow_empty or value.strip() != "":
            break
    return value

def int_input(question):
    while True:
        try:
            value = int(text_input(question))
        except ValueError:
            pass
        else:
            return value
        print("Please enter an integer")


def positive_int_input(question):
    while True:
        value = int_input(question)
        if value >= 0:
            return value
        print("Please enter a positive integer")

def choose_yes_no():
    while True:
        try:
            index = str_to_bool(text_input("Y(es)/N(o)"))
        except ValueError:
            print("Invalid option.  Please try again.")
        else:
            break

def choose_one_from_list(l, allow_exit=False): 
    for index, item in enumerate(l):
        print "\t{} - {}".format(index + 1, item)

    while True:
        index = int_input("Choose an option by number: ") - 1
        if allow_exit and index == -1:
            return None

        if index >= 0 and index < len(l):
            return (index, l[index])

        print("Invalid option.  Please try again.")

def choose_many_from_list(l):
    choices = []
    while True:
        choice = choose_one_from_list(l, len(choices) > 0)

        if choice == None:
            # User asked to exit the loop
            break

        l.pop(choice[0])
        choices.append(choice)

        if len(l) == 0:
            # All options have been selected
            break

    return choices

def choose_size (model, size_dic): 
    print "Selection of Sizes for model", model, ":"
    for size in size_dic: 
        print "SIZE: \t{} \tWEIGHT: \t{} \tCOST: \t{}" .format (size, size_dic[size][0], size_dic[size][1])
    choice = raw_input("Selected size:\t")
    while not(size_dic.__contains__(choice)): # choice not in size_dic: 
        print "Please type a valid size from list."
        choice = raw_input("Selected size:\t")
    return choice
