from pyscript import display, document

def team(e):
    document.getElementById('output').innerHTML = " "

    grade = document.getElementById('grade').value
    section = document.getElementById('section').value

    reg_com = document.getElementById('req').checked
    med_com = document.getElementById('med').checked

    if reg_com == False:
        display(f'Please complete the online requirements.', target='output')
    elif med_com == False:
        display(f'Please get a medical certificate first.', target='output')
    elif grade == "0":
        display(f'Please input your grade.', target='output')
    else:
        if section == "emerald":
            team = "Blue Bears"
        elif section == "ruby":
            team = "Red Bulldogs"
        elif section == "sapphire":
            team = "Green Hornets"
        elif section == "topaz":
            team = "Yellow Tigers"
        display(f'You are a part of the ' + team + ', Good luck on the Intramurals!', target='output')
