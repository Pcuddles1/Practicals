
import os


def main():

    os.chdir('Lyrics\Christmas\Temp')

    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            current_name = os.path.join(directory_name, filename)
            print(current_name)
            get_fixed_filename(filename)

def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    for letter in filename:
        if letter.isupper():
            new_name = filename.()
    print(new_name)

main()
