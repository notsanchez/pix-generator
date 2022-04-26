import webbrowser
import requests
import os
import clipboard

def clear():
    os.system("cls")

while True: 
    print("[1] - CPF")
    print("[2] - Email")
    print("[3] - CNPJ")
    print("[4] - Aleatória")

    tipo = input("Qual o tipo da chave: ")
    clear()

    chave = input("Digite a chave: ")
    clear()

    nome = input("Primeiro Nome: ")
    clear()

    valor = input("Valor (Exemplo: 10.00): ")
    clear()

    webhook_url = input("Link do webhook discord: ")

    if tipo == "1" or "2" or "3" or "4":
        url = 'https://gerarqrcodepix.com.br/api/v1?nome='+nome+'&cidade=Brasil&valor='+valor+'&saida=br&chave='+chave+'&txid='+nome

        qr_url = 'https://gerarqrcodepix.com.br/api/v1?nome='+nome+'&cidade=Brasil&valor='+valor+'&saida=qr&chave='+chave+'&txid='+nome
    else:
        pass

    response = requests.get(url)

    responsejson = response.json()
    pix_code = responsejson["brcode"]

    print("Seu Código pix é: "+pix_code)
    print("")
    print("Já está no seu CTRL + V :)")
    clipboard.copy(pix_code)

    webbrowser.open(qr_url)
    
    data = {
        "content": qr_url
    }

    result = requests.post(webhook_url, json=data)

    input("Pressione enter....")
    clear()