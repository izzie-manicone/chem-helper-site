#Any Imports Will Go Up Here
from dataclasses import dataclass
from drafter import *
from bakery import assert_equal

#Prep to Deploy
set_website_title("Chemistry Helper")
set_site_information(
    author="Izzie Manicone",
    description="Get help with basic chemistry operations",
    sources="Thanks to my drafter docs, mmy friends, google, and Dr Barts Chat Bot",
    planning=["plan.pdf", "design.pdf"],
    links=["https://github.com/your-username/your-repository"]
)

#Dictionary of Elements
ATOMIC_MASSES = {
    "H": 1.008,
    "He": 4.0026,
    "Li": 6.94,
    "Be": 9.0122,
    "B": 10.81,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "F": 18.998,
    "Ne": 20.180,

    "Na": 22.990,
    "Mg": 24.305,
    "Al": 26.982,
    "Si": 28.085,
    "P": 30.974,
    "S": 32.06,
    "Cl": 35.45,
    "Ar": 39.948,
    "K": 39.098,
    "Ca": 40.078,

    "Sc": 44.956,
    "Ti": 47.867,
    "V": 50.942,
    "Cr": 51.996,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.933,
    "Ni": 58.693,
    "Cu": 63.546,
    "Zn": 65.38,

    "Ga": 69.723,
    "Ge": 72.630,
    "As": 74.922,
    "Se": 78.971,
    "Br": 79.904,
    "Kr": 83.798,
    "Rb": 85.468,
    "Sr": 87.62,
    "Y": 88.906,
    "Zr": 91.224,

    "Nb": 92.906,
    "Mo": 95.95,
    "Tc": 98.0,
    "Ru": 101.07,
    "Rh": 102.906,
    "Pd": 106.42,
    "Ag": 107.868,
    "Cd": 112.414,
    "In": 114.818,
    "Sn": 118.710,

    "Sb": 121.760,
    "Te": 127.60,
    "I": 126.904,
    "Xe": 131.293,
    "Cs": 132.905,
    "Ba": 137.327,
    "La": 138.905,
    "Ce": 140.116,
    "Pr": 140.908,
    "Nd": 144.242,

    "Pm": 145.0,
    "Sm": 150.36,
    "Eu": 151.964,
    "Gd": 157.25,
    "Tb": 158.925,
    "Dy": 162.500,
    "Ho": 164.930,
    "Er": 167.259,
    "Tm": 168.934,
    "Yb": 173.045,

    "Lu": 174.967,
    "Hf": 178.49,
    "Ta": 180.948,
    "W": 183.84,
    "Re": 186.207,
    "Os": 190.23,
    "Ir": 192.217,
    "Pt": 195.084,
    "Au": 196.967,
    "Hg": 200.592,

    "Tl": 204.38,
    "Pb": 207.2,
    "Bi": 208.980,
    "Po": 209.0,
    "At": 210.0,
    "Rn": 222.0,
    "Fr": 223.0,
    "Ra": 226.0,
    "Ac": 227.0,
    "Th": 232.038,

    "Pa": 231.036,
    "U": 238.029,
    "Np": 237.0,
    "Pu": 244.0,
    "Am": 243.0,
    "Cm": 247.0,
    "Bk": 247.0,
    "Cf": 251.0,
    "Es": 252.0,
    "Fm": 257.0,

    "Md": 258.0,
    "No": 259.0,
    "Lr": 266.0,
    "Rf": 267.0,
    "Db": 268.0,
    "Sg": 269.0,
    "Bh": 270.0,
    "Hs": 277.0,
    "Mt": 278.0,
    "Ds": 281.0,

    "Rg": 282.0,
    "Cn": 285.0,
    "Nh": 286.0,
    "Fl": 289.0,
    "Mc": 290.0,
    "Lv": 293.0,
    "Ts": 294.0,
    "Og": 294.0
}

#dataclasses being defined
@dataclass
class Reaction:
    balanced_equation: str
    limiting_reactant: str
    theory_yield: float
    
@dataclass
class State:
    balanced_equation: str
    reactant_mass: str
    real_yield: float
    result_text: str 
    reactions: list[Reaction]
    heat_of_reaction: str
    heat_result: str
    
#Home page route
@route
def index(state: State) -> Page:
    """
    Shows the home page of the helper
    
    Args:
        state(State) - The class icluding the state of many attributes used in calculations
    
    Return:
        Page - Returns by showing the home page
    """
    return Page(state, [
        Header("Chemistry Helper Tool"),
        Text("With this tool you can calculate theoretical yield, percent yield,"
             " limiting reactants, and the heat of reaction."),
        Text("\nInstructions for Calculator:"),
        LineBreak(),
        #LineBreak breaks up your lines
        Text("\n1.Enter a balanced chemical equation in the following format"),
        LineBreak(),
        Text("\nEx. 2H2 + O2 -> 2H20"),
        LineBreak(),
        Text("\n2.Enter the masses of each reactant in the following format"),
        LineBreak(),
        Text("\nEx. H2: 4.032,O2: 32.00"),
        LineBreak(),
        Text("\n3.Enter the actual prooduct yield (of the first product) in the following format"),
        LineBreak(),
        Text("\nEx. 30.0"),
        LineBreak(),
        Text("\n4.Click save"),
        LineBreak(),
        Text("\n5.Click Calculate"),
        LineBreak(),
        Button("Go to the Calculator",calculator),
        Button("View History", history)])


#Page to get user input about the reaction
@route
def calculator(state: State) -> Page:
    """
    Page for the user to enter the reaction they want help with.
    
    Args:
        state(State) - The class icluding the state of many attributes used in calculations.
        They are updated throught the use of this page and its TextBoxes and Buttons.
    
    Return:
        Page - Returns by showing the calculator page
    """
    return Page(state, [
        Header("Information About Your Reaction"),
        #Div creates seperate sections
        Div(Text("Please enter your balanced chemical equation"),
        TextBox("balanced_equation", state.balanced_equation)),
        Div(Text("\nPlease enter the starting reactant masses"),
        TextBox("reactant_mass", state.reactant_mass)),
        Div(Text("\nPlease enter the actual yield of products in grams"),
        TextBox("real_yield", str(state.real_yield))),
        Button("Save All Inputs" ,save_inputs),
        Button("Calculate your Results",calculate)])

#Replacing the above update functions
@route
def save_inputs(state: State, balanced_equation: str, reactant_mass:str,
                real_yield: str) -> Page:
    """
    Saves all the inputs in the calculate function
    
    Args;
        state(State) - the current state
        balanced_equation(str) - the input balanced equation
        reactant_ mass(str) - the masses of reactants
        real_yield(str) - the input real yield
    Return:
        Page - calculator page with updated states
    """
    state.balanced_equation = balanced_equation
    state.reactant_mass = reactant_mass
    state.real_yield = float(real_yield)
    return calculator(state)

#Helper functions for calculating
def seperate_masses(reactant_mass: str) -> dict[str,float]:
    """
    Takes a string of reactants and their masses and creates a dictionary consisting of a
    string (to show the name of compound) and a float (to show the weight of that compound)
    
    Args:
        reactant_mass(str) - A string entered by the user showing reactants and their respective
        masses. This is also the same as state.reactant_mass.
    
    Return:
        dict[str, float] - Returns a dictionary of compounds and their wieghts for this reaction
    """
    masses = {}
    reactants = reactant_mass.split(",")
    for reactant in reactants:
        name, mass = reactant.split(":")
        masses[name.strip()] = float(mass.strip())
    return masses

#Helper functions added after chempy broke
def calculate_mass(formula: str, index: int) -> tuple[float, int]:
    mass = 0.0
    while index < len(formula):
        character = formula[index]
        if character == ")":
            return mass, index + 1
        elif character == "(":
            group_mass, index = calculate_mass(formula, index + 1)
            number = ""
            while index < len(formula) and formula[index].isdigit():
                number += formula[index]
                index += 1
            if number:
                mass += group_mass * int(number)
            else:
                mass += group_mass
        else:
            element = character
            index += 1
            if index < len(formula) and formula[index].islower():
                element += formula[index]
                index += 1
            number = ""
            while index < len(formula) and formula[index].isdigit():
                number += formula[index]
                index += 1
            if number:
                mass += ATOMIC_MASSES[element] * int(number)
            else:
                mass += ATOMIC_MASSES[element]
    return mass, index

def find_molar_mass(formula: str) -> float:
    """
    Finds the molar mass of a compound or element.

    Args:
        formula (str): The chemical formula of the compound.

    Returns:
        float: The molar mass of the compound.
    """
    molar_mass, index = calculate_mass(formula, 0)
    return molar_mass

#Back to normal helper functions
def find_mols(mass:float, molar_mass: float) -> float:
    """
    Finds the mols of a certain element in the reaction
    
    Args:
        mass(float) - The reactant mass of the element
        molar_mass(float) - The elements molar mass
    
    Return:
        float - the molar mass of the compound entered
    """
    mols = mass/molar_mass
    return mols

def find_coeffs(equation: str) -> dict[str, int]:
    """
    Fetches the coefficients in the balanced reaction
    
    Args:
        equation(str) - The balanced chemical equation.
        
    Return:
        dict[str,int] - Dictionary of reactants and their coefficients
    """
    coeffs = {}
    reactants = equation.split("->")[0]
    reactants = reactants.split("+")
    for reactant in reactants:
        reactant = reactant.strip()
        number = ""
        formula = ""
        for character in reactant:
            if character.isdigit() and formula == "":
                number = number + character
            else:
                formula = formula + character
        if number == "":
            coeffs[formula] = 1
        else:
            coeffs[formula] = int(number)
    return coeffs

def find_product_coeffs(equation: str) -> dict[str,int]:
    """
    Finds the products coefficients
    
    Args:
        equation: The balanced chemical equation
    
    Return:
        dict[str,int] - products formula and their coeffs
    """
    coeffs = {}
    products = equation.split("->")[1]
    products = products.split("+")
    for product in products:
        product = product.strip()
        number = ""
        formula = ""
        for character in product:
            if character.isdigit() and formula == "":
                number = number + character
            else:
                formula = formula + character
        if number == "":
            coeffs[formula] = 1
        else:
            coeffs[formula] = int(number)
    return coeffs
    
#Helper functions for calculating cont.
def find_limiting_reactant(mols: dict[str, float], coeffs: dict[str, int]) -> str:
    """
    Finds the limiting reactant in the entered reaction
    
    Args:
        mols(dict[str,float]): Mols of each reactant
        coeffs(dict[str,int]): Coefficients of each reactant
    
    Return:
        str - the formula of the limiting reactant
    """
    limiting = ""
    smallest_ratio = float("inf")
    for reactant in mols:
        ratio = mols[reactant]/coeffs[reactant]
        if ratio < smallest_ratio:
            smallest_ratio = ratio
            limiting = reactant
    return limiting

def calc_theory_yield(limiting: str, mols: dict[str, float],
                      reactant_coeffs: dict[str,int], product: str,
                      product_coeff: int) -> float:
    """
    Calculates the theoretical yield of a product(in grams)
    
    Args:
        limiting(str) - Limiting reactant
        mols(dict[str,float]) - mols of each reactant
        reactant_coeffs(dict[str,int]) - Coefficients of each reactant
        product(str) - Formula of the product
        product_coeff (int) - Coefficient of the product
    Return:
        float: The theortical yield(in grams)
    """
    limiting_mols = mols[limiting]
    limiting_coeff = reactant_coeffs[limiting]
    product_mols = limiting_mols * product_coeff / limiting_coeff
    theory_yield = product_mols * find_molar_mass(product)
    return theory_yield

def find_remaining_masses(limiting:str, mols: dict[str, float],
                          coeffs: dict[str,int])-> dict[str, float]:
    """
    Finds the remaining mass of each reactant
    
    Args:
        limiting(str) - the limiting reactant
        mols(dict[str, float]) - Starting mols of each reactant
        coeffs(dict[str,int])- Reactant coeffs
    Return:
        dict[str, float] - remaining masses of each reactant(in grams)
    """
    remaining = {}
    reaction_mols = mols[limiting] / coeffs[limiting]
    for reactant in mols:
        mols_used = reaction_mols*coeffs[reactant]
        leftover_mols = mols[reactant] - mols_used
        remaining[reactant] = max(0.0, leftover_mols) * find_molar_mass(reactant)
    return remaining
    
# Route for calculating
@route
def calculate(state:State) -> Page:
    """
    The function to do the basic calculations (Not Thermo)
    
    Args:
        state(State) - The class icluding the state of many attributes used in calculations.
        These attributes are used in the calculations.
    
    Return:
        Page - Returns by showing the results page with an updated state
    """
    masses = seperate_masses(state.reactant_mass)
    mols = {}
    for formula, mass in masses.items():
        molar_mass = find_molar_mass(formula)
        mols[formula] = find_mols(mass, molar_mass)
    coeffs = find_coeffs(state.balanced_equation)
    limiting = find_limiting_reactant(mols, coeffs)
    products = find_product_coeffs(state.balanced_equation)
    product = list(products.keys())[0]
    #keys() is used to take out one type from a dictionary (formulas in this case)
    product_coeff= products[product]
    theory_yield = calc_theory_yield(limiting, mols , coeffs, product, product_coeff)
    percent_yield = (state.real_yield/theory_yield) * 100
    remaining = find_remaining_masses(limiting, mols, coeffs)
    remaining_result_text = "\nRemaining Reactant Masses:"
    for reactant, mass in remaining.items():
        remaining_result_text = (remaining_result_text + "\n" + reactant+": "+
                                 str(round(mass, 3)) + " g")
    state.result_text = ("Limiting Reactant: " + limiting + "\nTheoretical Yield: " +
                         str(round(theory_yield, 3)) + " g"+"\nPercent Yield: "+
                         str(round(percent_yield,2))+ "%"+ remaining_result_text)
    #round(item, places after decimal)
    new_reaction = Reaction(state.balanced_equation,
                            limiting,
                            theory_yield)
    state.reactions.append(new_reaction)
    return results(state)

#Results Page
@route
def results(state: State) -> Page:
    """
    Page for the user to view the results of the calculation
    
    Args:
        state(State) - The class that includes the result text that will be displayed 
    
    Return:
        Page - Returns by showing the results page
    """
    return Page(state, [
        Header("Results"),
        # * is to  take items form a list and shows individually (using to separate lines)
        *[Div(Text(line)) for line in state.result_text.split("\n")],
        Button("New Calculation", calculator),
        Button("View Thermo", thermo),
        Button("Back to Home", index)])

#History Page
@route
def history(state: State) -> Page:
    """
    Page for the user to view the reactions that they previously entered
    
    Args:
        state(State) - The class that includes the list of previously entered
    reactions
    
    Return:
        Page - Returns by showing the history page and the list of previous
    reactions
    """
    previous_reactions = []
    for reaction in state.reactions:
        previous_reactions.append(
            Div(Text(reaction.balanced_equation + " | "),
                Text("Limiting Reactant: " + reaction.limiting_reactant + " | "),
                Text("Theoretical Yield: " +
                     str(round(reaction.theory_yield,3)) + " g")))
    return Page(state, [
        Header("History"),
        Header("Previous Reactions:"),
        *previous_reactions,
        Button("Back to Home", index)])

#Thermo Page
@route
def thermo(state:State) -> Page:
    """
    Page for the user to enter and calculate the heat of an entered reaction
    
    Args:
        state(State) - The class that hold the state of several important attributes
        for calculation
    
    Return:
        Page - Returns by showing the thermo page and its inputs and buttons
    """
    return Page(state, [
        Header("Thermochemistry"),
        Div(Text("First enter heat of reaction, then press 'Save Heat',"+
                 "then press 'Calculate Heat'")),
        Text("Heat of Reaction:"),
        TextBox("heat_of_reaction", state.heat_of_reaction),
        Button("Save Heat", update_heat),
        Button("Calculate Heat", calculate_heat),
        Text(state.heat_result),
        Button("Back to Home", index)])

#Update routes for thermo Page
@route
def update_heat(state:State, heat_of_reaction: str) -> Page:
    """
    Updates the heat_of_reaction in our state
    
    Args:
        state(State) - The class holding the heat_of_reaction and all our
        other info
        heat_of_reaction(str) - The value of heat entered by the user
    
    Return:
        Page - Displays the Thermo page but with an updated state
    """
    state.heat_of_reaction = heat_of_reaction
    return thermo(state)

@route
def calculate_heat(state:State) -> Page:
    """
    Calculates the total heat of the chemical reaction
    
    Args:
        state(State) - The class holding the heat_of_reaction and reactant
        info
    
    Return:
        Page - Displays the Thermo page but with the calculated heat
    """
    if state.heat_of_reaction.strip == "":
        return thermo(state)
    heat = float(state.heat_of_reaction)
    limiting = state.reactions[-1].limiting_reactant
    masses= seperate_masses(state.reactant_mass)
    molar_mass = find_molar_mass(limiting)
    mols = find_mols(masses[limiting], molar_mass)
    coeffs = find_coeffs(state.balanced_equation)
    limiting_coeff = coeffs[limiting]
    reaction_mols = mols/limiting_coeff
    total_heat = reaction_mols * heat
    state.heat_result = str(round(total_heat, 3)) + " kJ"
    return thermo(state)

#ASSERT_EQUAL TESTS
#Fake State used for testing
test_state = State(balanced_equation = "2H2 + O2 -> 2H2O",
                   reactant_mass = "H2: 4.032, O2:32.00",
                   real_yield = 30.0,
                   result_text = "",
                   reactions = [],
                   heat_of_reaction = "",
                   heat_result = "")
#Route tests
#Home (index) route
assert_equal(isinstance(index(test_state),Page),True)
#Calculator route
assert_equal(isinstance(calculator(test_state),Page),True)
#Calculate route
assert_equal(isinstance(calculate(test_state),Page),True)
#history route
assert_equal(isinstance(history(test_state),Page),True)
#results route
assert_equal(isinstance(results(test_state),Page),True)
#Thermo route
assert_equal(isinstance(thermo(test_state),Page),True)
# save_inputs route
assert_equal(test_state.balanced_equation, "2H2 + O2 -> 2H2O")
assert_equal(test_state.real_yield, 30.0)
assert_equal(test_state.reactant_mass, "H2: 4.032, O2:32.00")
test_page = save_inputs(test_state,
                         "2H2 + O2 -> 2H20",
                         "H2: 4.032, O2:32.00",
                         "30.0")
assert_equal(isinstance(test_page,Page),True)
#calculate_heat route
heat_state = State(balanced_equation = "2H2 + O2 -> 2H2O",
                   reactant_mass = "H2: 4.032, O2:32.00",
                   real_yield = 30.0,
                   result_text = "",
                   reactions = [Reaction("2H2 + O2 -> 2H2O", "O2", 36.032)],
                   heat_of_reaction = "-572",
                   heat_result = "")
heat_test_page = calculate_heat(heat_state)
assert_equal(isinstance(heat_test_page, Page),True)

#HELPER FUNCTION TESTS
#Seperate masses tests
assert_equal(seperate_masses("H2: 4.032, O2: 32.00"), {"H2": 4.032, "O2": 32.0})
assert_equal(seperate_masses("C2: 4.032, O2: 32.00"), {"C2": 4.032, "O2": 32.0})
#calculate masses tests
assert_equal(round(calculate_mass("O2",0)[0],3),32.0)
assert_equal(round(calculate_mass("O",0)[0],3),16.0)
#find molar mass tests
assert_equal(find_molar_mass("O2"), 32.0)
assert_equal(round(find_molar_mass("H2O"),3), 18.016)
#find mols tests
assert_equal(find_mols(10.0,10.0),1.0)
assert_equal(find_mols(20.0,10.0),2.0)
#find coeffs tests
assert_equal( find_coeffs("2H2 + O2 -> 2H2O"), {"H2": 2, "O2": 1})
assert_equal( find_coeffs("C + O2 -> CO2"), {"C": 1, "O2": 1})
#find product coeffs tests
assert_equal( find_product_coeffs("2H2 + O2 -> 2H2O"), {"H2O": 2})
assert_equal( find_product_coeffs("C + O2 -> CO2"), {"CO2": 1})
#find limiting reactant tests
assert_equal(find_limiting_reactant({"H2": 1.0, "O2": 1.0},{"H2": 2, "O2":1}),"H2")
assert_equal(find_limiting_reactant({"H2": 10.0, "O2": 1.0},{"H2": 2, "O2":1}),"O2")
#calc theory yield tests
assert_equal(round(calc_theory_yield("H2", {"H2": 1.0, "O2": 1.0}, {"H2": 2, "O2":1},
             "H2O",2), 3), 18.016)
assert_equal(round(calc_theory_yield("H2", {"H2": 1.0, "O2": 1.0}, {"H2": 2, "O2":1},
             "H2O",2), 3), 36.032)
#find remaining masses tests
remaining_test_one = find_remaining_masses("H2", {"H2": 1.0, "O2": 1.0}, {"H2": 2, "O2":1})

assert_equal(round(remaining_test_one["H2"],3),0.0)
assert_equal(round(remaining_test_one["O2"],3),16.0)

remaining_test_two = find_remaining_masses("H2", {"H2": 1.0, "O2": 1.0}, {"H2": 2, "O2":1})

assert_equal(round(remaining_test_two["H2"],3),16.128)
assert_equal(round(remaining_test_two["O2"],3),0.0)

#START SERVER
start_server(State("","",0.0,"",[], "", ""))       
