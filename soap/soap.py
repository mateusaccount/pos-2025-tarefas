import requests
from xml.dom.minidom import parseString

URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

def get_country_iso_code(country_name):
    body = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xmlns:xsd="http://www.w3.org/2001/XMLSchema"
               xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CountryISOCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryName>{country_name}</sCountryName>
    </CountryISOCode>
  </soap:Body>
</soap:Envelope>"""

    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CountryISOCode"
    }

    response = requests.post(URL, data=body, headers=headers)
    dom = parseString(response.text)
    iso_code = dom.getElementsByTagName("m:CountryISOCodeResult")[0].firstChild.nodeValue
    return iso_code