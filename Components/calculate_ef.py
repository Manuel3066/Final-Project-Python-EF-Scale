from Components import Gui


def calculate_ef(user_Input):
    user_input = 0

    try:
        if type(user_Input) is not int:
            raise ValueError
    except ValueError:
        print("a non numerical value was entered")

    user_input = user_Input
    if 65 <= user_input <= 85:
        Gui.ef0()
    elif 86 <= user_input <= 110:
        Gui.ef1()
    elif 111 <= user_input <= 135:
        Gui.ef2()
    elif 136 <= user_input <= 165:
        Gui.ef3()
    elif 166 <= user_input <= 200:
        Gui.ef4()
    elif user_input > 200:
        Gui.ef5()
    else:
        print("Please only enter a number within range")

