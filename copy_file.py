from shutil import copyfile

def copy_file(x):
    source_file = r"C:/Users/elies/Downloads/selfie.png"
    destination_file = "C:/Users/elies/Downloads/selfies/selfie{}.png".format(x)

    copyfile(source_file, destination_file)
    print("{} copied to {}".format(source_file, destination_file))
    return None

def copy_file2():
    source_file = r"C:/Users/elies/Downloads/selfie.png"
    destination_file = r"C:/Users/elies/Documents/GitHub/Quiz_Avengers/static/img/selfie.png"

    copyfile(source_file, destination_file)
    print("{} copied to {}".format(source_file, destination_file))
    return None
