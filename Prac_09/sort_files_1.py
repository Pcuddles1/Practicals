import os


os.chdir('FilesToSort')

directorys = []
for directory_name, subdirectories, filenames in os.walk('.'):



    for filename in filenames:
        current_name = os.path.join(directory_name, filename)
        print(current_name)
        directorys.append(filename[filename.find('.'):])
    for directory in directorys:
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass
        os.chdir(directory)
        shutil.move(filename)





