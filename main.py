#! /usr/bin/python3
from git import gitStatus, gitAdd, gitCommit, gitPush


def main():

    out = gitStatus()
    while True:
        word = input('Digite o número do exercício[exX.cpp]:')
        if out.find(word) != -1:
            gitAdd(word)
            gitCommit(word)
            gitPush()
            break
        else:
            word = input('Digite o número do exercício[exX.cpp]:')


if __name__ == '__main__':
    main()
    print('fim')
