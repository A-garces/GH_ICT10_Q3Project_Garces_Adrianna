from pyscript import display, document

sapphire_players = [
    "Tessa Ysabelle Marzan Aseo", "Anakin Miguel Quinto Batac", 
    "Neriza Alipio Calanglang", "Vito Antonio Olivera De Guzman",
    "Aaron James Gonzalo Dee", "Harvey Wayne Batino Dolor", 
    "Selena Mansueto Galvez", "Adrianna Malanum Garces", 
    "Jillian Cuison Grospe", "Eduardo Alonso Magsombol Hizon",
    "Margo Zera Francisco Intalan", "Atasha Soleil Romero Ko", 
    "Alijah Rain Lagman", "Marcus Christian Panlilio Law",
    "Sittie Ainah Mariano Macabago", "Euan Justin Lim Martinez", 
    "Kelsey Claire Lago Medina", "Michaela Ysabelle Cayno Mendoza",
    "Manuel Jacinto Guarino Mergal", "Seth Garett Gomez Ngo", 
    "Sofia Laurence Fabella Padojinog", "Benigno Ignacio Jhocson Rivera",
    "Ishan Justice Quiambao Shrestha", "Jennifer Lorraine Sanchez Uy", 
    "Francesca Jean Kho Yao"
]

def show_players(event):
    
    display("Sapphire: Green Hornets", target="output")

    output = document.getElementById("output")
    output.innerHTML = ""
    
    for i, name in enumerate (sapphire_players, 1):
        formatted_name = f"{i}) {name}"
        display(formatted_name, target="output")

button = document.querySelector("button")

