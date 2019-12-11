from Components.calculate_ef import calculate_ef
from Components.file_write import write_to_file
from Objects.main_parent import main_parent


class main_child(main_parent):

    def __init__(self,location="Default", population="0"):
        self._location = location
        self._population = population

    def gui_out(self,input):
        calculate_ef(input)

    def set_population(self,population):
        self._population = population

    def set_location(self,location):
        self.location = location


    def main_run(self):
        user_input = 0

        print("Welcome this program shall check the wind speed you enter")
        print("And show you where it is on the EF Scale and help you determine the danger")
        print("Once you are finished with the program there should be a txt file showing your history")
        while user_input != -999:
            print("Please enter a value between 65 and above")
            print("Or enter a -999 to quit out of the program")
            buffer_value = int(input())
            if buffer_value == -999:
                break
            else:
                user_input = buffer_value
            self.gui_out(user_input)


        print("Good Bye and Stay Safe!")
