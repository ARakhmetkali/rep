
import pathlib
import os
import os.path
from string import ascii_uppercase

# task 1
def listDirs(p):
    print([x.name for x in os.scandir(path = p) if x.is_dir()])


def listFiles(p):
    print([x.name for x in os.scandir(path = p) if x.is_file()])


def listDirsAndFiles(p):
    print([x.name for x in os.scandir(path = p)])


# task 2
def checkPath(p):
    exist_status = os.access(path = p, mode = os.F_OK)
    print(f'Existance : {exist_status}')
    read_status = os.access(path = p, mode = os.R_OK)
    print(f'Radibility : {read_status}')
    write_status = os.access(path = p, mode = os.W_OK)
    print(f'Writability : {write_status}')
    exec_status = os.access(path = p, mode = os.X_OK)
    print(f'Executability : {exec_status}')

# task 3
def existAndRetrivePathInfo(p):
    exist_status = os.access(path = p, mode = os.F_OK)
    if exist_status:
        print(f'File : {os.path.basename(p)}')
        print(f'Directory : {os.path.dirname(p)}')
    else:
        print('Path is not executable')


# task 4
def countLines(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        count += 1
    return count


# task 5
def writeToFile(filename, new_list):
    file = open(filename, 'a')
    file.write(str(new_list))
    file.close()

    file = open(filename , 'r')
    print(file.read())


# task 6
def generateFiles():
    for char in ascii_uppercase:
        file = open(f'./files/{char}.txt', 'x')
        file.close()


# task 7
def copyContent(init_filename, target_filename):
    init_file = open(init_filename, 'r')
    file_content = init_file.read()
    init_file.close()

    target_file = open(target_filename, 'w')
    target_file.write(str(file_content))
    target_file.close()
    print('Successfully copied')

    target_file = open(target_filename, 'r')
    print(target_file.read())
    target_file.close()


# task 8
def deleteFile(p):
    if os.path.exists(p):
        os.remove(p)
        print('Successfully deleted the file')
    else:
        print('File does not exist')

def main():
    path = '..'
    print('Task 1')
    listDirs(path)
    listFiles(path)
    listDirsAndFiles(path)

    print('Task 2')
    checkPath(path)

    print('Task 3')
    existAndRetrivePathInfo('../SIS5/RegEx.py')

    print('Task 4')
    print(f'Number of lines in a file demofile.txt = {countLines("demofile.txt")}')

    print('Task 5')
    writeToFile('demofile2.txt', ['Hello', 'World'])

    print('Task 6')
    #generateFiles()

    print('Task 7')
    copyContent('demofile.txt', 'demofile3.txt')

    print('Task 8')
    deleteFile('./were.txt')

if __name__ == '__main__':
    main()