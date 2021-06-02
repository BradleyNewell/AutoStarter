import os
''' TODO: data folder with blank csv file
'''
paths_to_exe = [r'"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"',
                r'"C:\Program Files\Mozilla Firefox\firefox.exe"']


def execute(paths):
    for i in paths:
        try:
            os.system(i)
        except FileNotFoundError:
            print(f"File {str(i)} not found")


if __name__ == __main__:
    execute(paths_to_exe)
