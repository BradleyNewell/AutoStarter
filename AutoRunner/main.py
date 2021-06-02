import os
''' TODO: data folder with blank csv file
'''
paths_to_exe = [r'"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"',
                r'"C:\Program Files\Mozilla Firefox\firefox.exe"']


def execute():
    for i in paths_to_exe:
        try:
            os.system(i)
        except FileNotFoundError:
            print(f"File {str(i)} not found")

