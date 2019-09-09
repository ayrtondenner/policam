import os
from xml.dom import minidom
import xml.etree.ElementTree as ET

FINAL_XMLS_FOLDER = './resized_prints/final_folder/annotations/xmls'

xml_valid_files = [xml for xml in os.listdir(FINAL_XMLS_FOLDER) if xml.endswith('.xml')]

for i, xml_filename in enumerate(xml_valid_files):

    xml_path = os.path.join(FINAL_XMLS_FOLDER, xml_filename)

    xml_file = ET.parse(xml_path)
    #root = xml_file.getroot()

    for element in xml_file.findall('folder'):
        element.text = 'xmls'

    for element in xml_file.findall('filename'):
        element.text = xml_filename.replace('.xml', '.jpg')

    for element in xml_file.findall('path'):
        element.text = os.path.realpath(xml_path).replace('.xml', '.jpg')

    xml_file.write(xml_path)

    print("{}/{} xmls".format(i + 1, len(xml_valid_files)))
