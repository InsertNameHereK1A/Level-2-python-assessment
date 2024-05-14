# funtion that returns everything about the ingredient
def ingredientInfo():
  type = input("What ingredient do you want to add? ")
  amount = input("How much of the ingredient do you want to add? ")
  cost = input("How much does it cost? $")
  return [type, amount, cost]
  
def MoreIngredients():
  MoreIngredients = input("Do you want to add more ingredients? ").lower()
  while True:
    if MoreIngredients == "no":
      return False
    if MoreIngredients == "yes":
      return True
    else:
      
      MoreIngredients = input("Do you want to add more ingredients? ").lower()
    
#WELCOME THE USER
print('''
 ██╗       ██╗███████╗██╗      █████╗  █████╗ ███╗   ███╗███████╗  ██╗   ██╗ ██████╗███████╗██████╗ 
 ██║  ██╗  ██║██╔════╝██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝  ██║   ██║██╔════╝██╔════╝██╔══██╗
 ╚██╗████╗██╔╝█████╗  ██║     ██║  ╚═╝██║  ██║██╔████╔██║█████╗    ██║   ██║╚█████╗ █████╗  ██████╔╝
  ████╔═████║ ██╔══╝  ██║     ██║  ██╗██║  ██║██║╚██╔╝██║██╔══╝    ██║   ██║ ╚═══██╗██╔══╝  ██╔══██╗
  ╚██╔╝ ╚██╔╝ ███████╗███████╗╚█████╔╝╚█████╔╝██║ ╚═╝ ██║███████╗  ╚██████╔╝██████╔╝███████╗██║  ██║
   ╚═╝   ╚═╝  ╚══════╝╚══════╝ ╚════╝  ╚════╝ ╚═╝     ╚═╝╚══════╝   ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
''')

#Getting variables

Recipe = []
RecipeTitle = input("What is the name of the recipe? ")
ServingSize = int(input("How many people does this recipe serve? "))
#Getting ingredients
GettingIngredients = True
while GettingIngredients is True:
#Asking if they want to add more ingredients
  Recipe.append(ingredientInfo())
  
  

#getting total cost per serving
TotalCostPerServing = 0
for i in range(0,len(Recipe)):
  TotalCostPerServing = TotalCostPerServing + int(Recipe[i][2])
print(TotalCostPerServing)