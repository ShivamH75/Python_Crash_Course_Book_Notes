# Storing Your Functions in Modules
# 'module' meaning - module - a unit that forms part of something bigger
#  functions can be kept seperated and stored in seperate file called module

# 'import' statement can be used to bring the function in the file we are working in 

#  in the working directory, add name of the file containing the functions
# To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make separated by a dot, 
# e.g. moduleName.functionName(arg1, arg2)

import pizza

pizza.createPizza(24, "non-veg", 'onion', 'pepperoni')



## We can also import specific functions from a Module
# syntax -    from module_name import function_name
# doing so, we dont need to add dot notation before the module name

from pizza import showToppings
 
showToppings('nonveg') 

## Using 'as' to Give a Function an Alias
# if there is some function or module in our file which has same name, we can use 'as'    

from pizza import showToppings as showTopp          # giving alias to 'function' name

showTopp('veg')

import pizza as pz                                  # giving alias to 'module' name

pz.showToppings('mixed')



## Importing All Functions in a Module
# use * symbol

from pizza import *

# However, The best approach is to import the function or functions you want, or import the entire module and use the dot notation