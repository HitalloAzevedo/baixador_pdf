author = 'Hitallo Azevedo'
version = 'v0.0.1'

import requests
from os import path, mkdir, listdir

folder_name = 'downloaded_files'

def exist():
    p = listdir()
    if folder_name not in p:
        return False    
    else:
        return True


def header(txt):
    print('=' * 60)
    print(txt.center(60))
    print('=' * 60)


def main():
    header(f'Baixador de PDF {version}')
    print(f'Criado por {author}')
    print('=' * 60)

    url = str(input('Link: ')).strip()
    name = str(input('Nome do arquivo: '))

    if exist() == True:
        pass
    else:
        mkdir(folder_name)

    p = path.join(folder_name, name+'.pdf')

    try:
        r = requests.get(url)
    except (requests.ConnectionError):
        print('Erro na conexão!')
    except(requests.RequestException):
        print('URL inválida!')
    else:
        print('Iniciando Download...')
        if r.status_code == 200:
            with open(p, 'wb+') as file:
                file.write(r.content)
            
            print(f'Download finalizado, salvo em: {p}')


if __name__ == '__main__':
    main()
