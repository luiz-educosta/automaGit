import os

REPO = '~/C202-ALG1'
GIT_STATUS = 'git -C ' + REPO + ' status'
GIT_ADD = 'git -C ' + REPO + ' add '
GIT_COMMIT = 'git -C ' + REPO + ' commit -m '
GIT_PUSH = 'git -C ' + REPO + ' push origin main'


def gitStatus():
    out = os.popen(GIT_STATUS).read()
    os.system(GIT_STATUS)
    return out


def gitAdd(word):
    os.system(GIT_ADD + 'teoria/entrada_e_saida_de_dados/ex' + str(word) + '.cpp')
    print('Git add Ok!')


def gitCommit(word):
    os.system(
        GIT_COMMIT + (f'"[Teoria/Cap1] Resolução do exercício {str(word)}."'))
    print('Git add Ok!')


def gitPush():
    os.system(GIT_PUSH)
    print('Git push Ok!')
