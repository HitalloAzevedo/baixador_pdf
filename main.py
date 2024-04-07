import requests
from os import path, mkdir, listdir

AUTHOR = 'Hitallo Azevedo'
VERSION = 'v0.0.2'

outputFolderName = 'download-output'

def existFile(folderName):
    if folderName in listdir():
        return True    
    else:
        return False

def header(txt, author, version):
    print('=' * 60)
    print('|' + txt.center(58) + '|')
    print('=' * 60)
    print(f'Created by {author}')
    print(f'Version: {version}')
    print('=' * 60)

def writeFile(outputPath, content):
    with open(outputPath, 'wb+') as file:
        file.write(content)

def main():
    header(f'PDF Downloader', AUTHOR, VERSION)

    fileUrl = str(input('Link do arquivo: ')).strip().lower()
    fileName = str(input('Nome do arquivo: ')).strip()

    if not existFile(outputFolderName):
        mkdir(outputFolderName)

    outputFilePath = path.join(outputFolderName, fileName + '.pdf')

    try:
        response = requests.get(fileUrl)
    except (requests.ConnectionError):
        print('Erro na conexão!')
    except (requests.RequestException):
        print('URL inválida!')
    except (Exception):
        print(f'Erro: {Exception}')
    else:
        if response.status_code == 200:
            print('Iniciando Download...')
            writeFile(outputFilePath, response.content)
            print(f'Download finalizado, salvo em: {outputFilePath}')
        else:
            print(response.status_code)

if __name__ == '__main__':
    main()
