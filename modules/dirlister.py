import os

def run(**args):
    print("[*] In dirlister module.")
    files = os.Listdir(".")
    return str(files)

