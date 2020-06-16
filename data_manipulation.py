#sort multiple list at once, utilizing the first argument as the sort rule
def sort_list(*args):

    #check to ensure length of all lists are the same making the first list the rule
    accept_length = len(args[0])
    len_ok = None

    for arg in args:
        if len(arg) != accept_length:
            len_ok = False
        else:
            len_ok = True

    if len_ok == True:
        #sort both list by first parameter
        args = sorted(zip(*args))

        #retrieves number of arguments passed
        length = len(args[0])

        #initializes new list for results to be returned as a tuple for multi-variable assignment
        results = []

        #counter starts index, creating each list
        counter = 0

        while counter < (length):
            #initialize new list to contain original list argument but sorted
            add_list = []

            for i in args:
                add_list.append(i[counter])

            #add each list to entire results list
            results.append(add_list)
            counter += 1

        return(tuple(results))

    else:
        print("***LISTS ARE NOT EQUAL***")


x = [1, 3, 5, 2, 4, 3 ]
z = ["one", "three", "five", "two", "four", "three"]
y = ["uno", "tres", "cinco", "dos", "quatro", "tres"]
n, i, o = sort_list(x, z, y)

print(n) #returns [1, 2, 3, 3, 4, 5]
print(i) #returns ["one", "two", "three", "three", "four", "five"]
print(o) #returns ["uno", "dos", "tres", "tres", "quatro", "cinco"]
