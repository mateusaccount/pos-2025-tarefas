from zeep import Client
#URL do WSDL
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

#Cria o cliente
client = Client(wsdl=wsdl_url)

def menu():
    try:
        number = int(input("Digite um número inteiro: "))
        result = client.service.NumberToWords(ubiNum=number)
        print(f"Número por extenso em inglês: {result}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
menu()