# Import required Modules

import os
import shutil

try:

    # take path from user

    path = input(r"Enter Path: ")
    files = os.listdir(path)

    for file in files:
        
        # extract extention from file name 

        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+'/' + extension):
            # if file.endswith(extension):
            shutil.move(path+'/'+file, path + '/' + extension)

        else:
            os.makedirs(path + '/' + extension)
            shutil.move(path+'/' + file, path + '/' + extension)

except:

    print("error")
