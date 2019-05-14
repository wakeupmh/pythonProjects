# -*- coding: utf-8 -*-
import acesso
global usr, passw
def inputs():
    print("\n\n################  BEM VINDO AO GERADOR DE LICENÇAS APPLE ###############\n")
    usr   = input("Digite o e-mail da sua conta Apple Developer:\n")
    if(usr.strip() == ''):
        print("#ERROR00 - Preencha todos os campos\n")
        usr = input("Digite o e-mail da sua conta Apple Developer:\n")
    passw = input("Digite a senha da sua conta Apple Developer:\n")
    if(passw.strip() == ''):
        print("#ERROR00 - Preencha todos os campos\n")
        passw = input("Digite a senha da sua conta Apple Developer:\n")
    optd  = input("Escolha uma opção:\n 1 - Desenvolvimento\n 2 - Produção\n 3 - Gerar ID\n")
    if(optd.strip() == ''):
        print("#ERROR00 - Preencha todos os campos\n")
        optd = input("Escolha uma opção:\n 1 - Desenvolvimento\n 2 - Produção\n 3 - Gerar ID\n")
    if(auth(usr, optd) > 0):
        inputs()
    else:

        if(optd == '1' or optd =='2'):
            alias = input("Digite o alias do seu app: \n")
            nCert = input("Digite o nome que deseja que seu Provisioning File tenha:\n")
        else:
            alias = input("Digite o alias do seu app (ex: com.desenvolvedor.nomeApp):\n")
            nCert = input("Digite o nome que deseja que seu App ID tenha:\n")
        acesso.acesso(usr, passw, optd, alias, nCert)


def inputsSemCred(usr, passw):
    optd = input("Escolha uma opção:\n 1 - Desenvolvimento\n 2 - Produção\n 3 - Gerar ID\n")
    if (optd.strip() == ''):
        print("#ERROR00 - Preencha todos os campos\n")
        optd = input("Escolha uma opção:\n 1 - Desenvolvimento\n 2 - Produção\n 3 - Gerar ID\n")
    if (auth(usr, optd) > 0):
        inputs()
    else:
        if(optd == '1' or optd =='2'):
            alias = input("Digite o alias do seu app: \n")
            nCert = input("Digite o nome que deseja que seu Provisioning File tenha:\n")
        else:
            alias = input("Digite o alias do seu app (ex: com.desenvolvedor.nomeApp):\n")
            nCert = input("Digite o nome que deseja que seu App ID tenha:\n")
        acesso.acesso(usr, passw, optd, alias, nCert)

def auth(usr, optd):
    error = 0
    if(usr.find('@') < 0 and usr.find('.') < 0):
        print('#ERROR01 - Digite um e-mail válido!!!\n')
        error+1
    if (optd.isdigit() == False):
        print('#ERROR02 - Digite um valor válido!!!\n')
        error+1
    return error

def main():
    inputs()

if __name__ == '__main__':
    main()