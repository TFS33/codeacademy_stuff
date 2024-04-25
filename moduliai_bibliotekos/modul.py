def counting_numbers(x):
    y = x * x
    print(f'{x} * {x} = {y}')


def capitalize_string(f):
    return f.capitalize()

def sorted_list(v):
    return sorted(v)


def root(numb):
    return numb ** 2



if __name__ == "__main__":
    text = input("Skirtas testavimui ar veikia")
    print(text)

import pyjokes
def get_joke():
    print(pyjokes.get_joke())




import os


"""
os.listdir()
os.mkdir()
os.mknod()
os.rename()
os.path.exists()
os.path.join()
os.remove()
"""


def show_names_from_files():
    return os.listdir()

print(show_names_from_files())


def show_names_from_files():
    os.mkdir('N:/testas')

show_names_from_files()


os.mknod('N:/testas.unk')