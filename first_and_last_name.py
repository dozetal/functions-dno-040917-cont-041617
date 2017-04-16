
# Part 1b: What's your name?
# Define first and last name

first_name = "Michelle"
last_name = "Obama"

def first_and_last_name(first_name, last_name):
    """
    Prompts for first and last name
    Concatenates and returns both names in one string 

    """

    # first attempt to return name 
    # uncomment the next line to confirm output
    # print (first_name) + " " + (last_name)
    # return (first_name) + " " + (last_name)

    name = ((first_name) + " " + (last_name))

    # second attempt to return name in usable form for Pt C
    # uncomment the next line to confirm output
    # print name
    return name

    
first_and_last_name(first_name, last_name)
