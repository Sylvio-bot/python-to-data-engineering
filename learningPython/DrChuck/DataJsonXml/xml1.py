import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Sylvio</name>
    <phone type="intl">
        +261 38 81 468 91
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Tel:', tree.find('phone').text.strip())
print('Attr',tree.find('email').get('hide'))
