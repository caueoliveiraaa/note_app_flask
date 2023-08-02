import os


def main():
    """ Atualizar requirements.txt e mostrar
    versões python / pip e mostrar dependências """

    os.system('cls')
    print('\033[032m')
    os.system('pip freeze > requirements.txt')
    print('--updated requirements.txt')
    os.system('python -m pip install --upgrade pip')
    os.system('pip freeze')
    os.system('pip --version')
    os.system('python --version')
    print('\033[0m')


if __name__ == '__main__':
    main()