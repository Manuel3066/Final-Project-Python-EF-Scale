import datetime



def zero():
    f = open("WindReport.txt", "a")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write("SPEED ENTERED IS IN THE LIGHT BLUE ZONE\n")
    f.write("RANGE BETWEEN 65-85\n")
    f.write("EXPECT LITTLE DAMAGE\n")
    f.write("\n\n")
    f.close()

def one():
    f = open("WindReport.txt", "a")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write("SPEED ENTERED IS IN THE LIGHT TAN ZONE\n")
    f.write("RANGE BETWEEN 86-110\n")
    f.write("EXPECT MINOR DAMAGE\n")
    f.write("\n\n")
    f.close()

def two():
    f = open("WindReport.txt", "a")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write("SPEED ENTERED IS IN THE TAN ZONE\n")
    f.write("RANGE BETWEEN 111-135\n")
    f.write("EXPECT FOR ROOF TO BE GONE\n")
    f.write("\n\n")
    f.close()

def three():
    f = open("WindReport.txt", "a")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write("SPEED ENTERED IS IN THE BROWN ZONE\n")
    f.write("RANGE BETWEEN 136-165\n")
    f.write("EXPECT WALLS TO COLLAPSE\n")
    f.write("\n\n")
    f.close()

def four():
    f = open("WindReport.txt", "a")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write("SPEED ENTERED IS IN THE ORANGE ZONE\n")
    f.write("RANGE BETWEEN 166-200\n")
    f.write("SEEK SHELTER AS HOUSES ARE EXPECTED TO BE BLOWN DOWN\n")
    f.write("\n\n")
    f.close()
def five():
    f = open("WindReport.txt", "a")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write("SPEED ENTERED IS IN THE RED ZONE\n")
    f.write("RANGE BETWEEN 201 and UP\n")
    f.write("SEEK SHELTER AS HOUSES ARE EXPECTED TO BE BLOWN AWAY\n")
    f.write("\n\n")
    f.close()


def write_to_file(argument):
    switcher = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
    }
    switcher[argument]()





