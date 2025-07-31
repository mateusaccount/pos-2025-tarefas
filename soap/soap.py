import requests
from xml.dom.minidom import parseString

URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

def soap_request(soap, versaoxml):
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": soap
    }
    response = requests.post(URL, data=versaoxml, headers=headers)
    return response.text

def moeda(country_code):
    versaoxml = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CountryCurrency>
      </soap:Body>
    </soap:Envelope>"""

    xml = soap_request("http://www.oorsprong.org/websamples.countryinfo/CountryCurrency", versaoxml)
    dom = parseString(xml)
    currency = dom.getElementsByTagName("m:sName")[0].firstChild.nodeValue
    print(f"Moeda de {country_code}: {currency}")

def capital(country_code):
    versaoxml = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CapitalCity>
      </soap:Body>
    </soap:Envelope>"""

    xml = soap_request("http://www.oorsprong.org/websamples.countryinfo/CapitalCity", versaoxml)
    dom = parseString(xml)
    capital = dom.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
    print(f"Capital de {country_code}: {capital}")

def idioma(country_code):
    versaoxml = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryLanguages xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_code}</sCountryISOCode>
        </CountryLanguages>
      </soap:Body>
    </soap:Envelope>"""

    xml = soap_request("http://www.oorsprong.org/websamples.countryinfo/CountryLanguages", versaoxml)
    dom = parseString(xml)
    languages = dom.getElementsByTagName("m:sName")
    print(f"Idiomas de {country_code}:")
    for lang in languages:
        print(f"- {lang.firstChild.nodeValue}")

#Menu
def menu():
    print("Escolha uma opção:")
    print("1 - Ver moeda do país")
    print("2 - Ver capital do país")
    print("3 - Ver idioma(s) do país")
    option = input("Digite o número da opção: ")
    code = input("Digite o código ISO do país (ex: BR, US, FR): ").upper()

    if option == "1":
        moeda(code)
    elif option == "2":
        capital(code)
    elif option == "3":
        idioma(code)
    else:
        print("Opção inválida.")

menu()