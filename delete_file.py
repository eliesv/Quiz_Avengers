import os

def delete_file(file_path):
    myfile = file_path

    if os.path.isfile(myfile):
        os.remove(myfile)
        print("file deleted")

    else:    ## Show an error ##
        print("Error: %s file not found" % myfile)

    return None    
