from shutil import copyfile
import os

def copy_file(x):
    pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads/selfie.png")
    source_file = pathSelfie

    pathSelfieDest=os.path.join(os.path.expanduser("~"), "Downloads/selfies/selfie{}.png".format(x))
    destination_file = pathSelfieDest

    copyfile(source_file, destination_file)
    print("{} copied to {}".format(source_file, destination_file))
    return None

def copy_file2():
    pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads/selfie.png")
    source_file = pathSelfie


    pathSelfieDest=os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/static/img/selfie.png")
    destination_file = pathSelfieDest

    copyfile(source_file, destination_file)
    print("{} copied to {}".format(source_file, destination_file))
    return None
