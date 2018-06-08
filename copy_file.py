from shutil import copyfile
import os

def copy_file(x):
    pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads\\selfie.png")
    pathSelfie=pathSelfie.replace("\\","/")
    source_file = pathSelfie

    pathSelfieDest=os.path.join(os.path.expanduser("~"), "Downloads\\selfie\\selfie{}.png".format(x))
    pathSelfieDest=pathSelfieDest.replace("\\","/")
    destination_file = pathSelfieDest

    copyfile(source_file, destination_file)
    print("{} copied to {}".format(source_file, destination_file))
    return None

def copy_file2():
    pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads\\selfie.png")
    pathSelfie=pathSelfie.replace("\\","/")
    source_file = pathSelfie


    pathSelfieDest=os.path.join(os.path.expanduser("~"), "Documents\\GitHub\\Quiz_Avengers\\static\\img\\selfie.png")
    pathSelfieDest=pathSelfieDest.replace("\\","/")
    destination_file = pathSelfieDest

    copyfile(source_file, destination_file)
    print("{} copied to {}".format(source_file, destination_file))
    return None
