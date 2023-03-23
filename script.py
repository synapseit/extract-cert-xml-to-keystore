import xml.etree.ElementTree as ET
import base64
import urllib.request

# Download the XML file from the URL
url = 'https://eidas.agid.gov.it/TL/TSL-IT.xml'
response = urllib.request.urlopen(url)
xml_data = response.read()

# Load the XML
tree = ET.ElementTree(ET.fromstring(xml_data))

# Find all X509 certificate elements
cert_elements = tree.findall('.//{http://uri.etsi.org/02231/v2#}X509Certificate')

# Loop through each certificate element and save the certificate to a file
for i, cert_element in enumerate(cert_elements):
    # Decode the certificate data from base64
    cert_data = base64.b64decode(cert_element.text)

    # Write the certificate data to a file
    with open(f'certificate_{i}.cer', 'wb') as cert_file:
        cert_file.write(cert_data)
