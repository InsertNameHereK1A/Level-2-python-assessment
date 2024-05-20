import json
import os


# loading the json file
def LoadJsonData(filename):
  if not os.path.exists(filename):
    with open(filename, 'w') as file:
      json.dump({}, file)

  with open(filename, 'r') as file:
    return json.load(file)


#saving the json file
def SaveJsonData(filename, data):
  with open(filename, 'w') as file:
    json.dump(data, file)


# funtion that returns everything about the ingredient
def ingredientInfo():
  type = input("What ingredient do you want to add? ")
  amount = input("How much of the ingredient do you want to add? ")
  cost = input("How much does it cost? $")
  return [type, amount, cost]


# funtion that ask if you would like to add mopre ingredients
def MoreIngredients():
  while True:
    MoreIngredients = input("Do you want to add more ingredients? ").lower()
    if MoreIngredients == "no":
      return False
    if MoreIngredients == "yes":
      return True
    print('invalid input')


# loading the json file
JsonFilename = 'recipe.json'
JsonData = LoadJsonData(JsonFilename)

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
RecipeTitle = input("What is the name of the recipe? ").lower()
#checking if the recipe is already in the json file
if RecipeTitle in JsonData:
  print("Recipe already exists")
  while True:
    output = input("Would you like to see the recipe? ")
    if output == "yes":
      print(JsonData[RecipeTitle])
      break
    elif output == "no":
      exit()
    else:
      print("invalid input")

ServingSize = int(input("How many people does this recipe serve? "))
#Getting ingredients
GettingIngredients = True
while GettingIngredients is True:
  #Asking if they want to add more ingredients
  Recipe.append(ingredientInfo())
  GettingIngredients = MoreIngredients()

#Saving the recipe

SaveJsonData('recipe.json', Recipe)
#getting total cost per serving
TotalCostPerServing = 0
for i in range(0, len(Recipe)):
  TotalCostPerServing = TotalCostPerServing + int(Recipe[i][2])
print(f"{RecipeTitle}'s cost per serving is {TotalCostPerServing}")
