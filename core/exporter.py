# crawler/exporter.py

import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

def export_to_xml(csv_file, xml_file):
    """Convert a CSV file of product changes to XML format."""
    try:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            root = ET.Element("products")

            for row in reader:
                product = ET.SubElement(root, "product")
                for key, value in row.items():
                    child = ET.SubElement(product, key)
                    child.text = value

            # Pretty print
            rough_string = ET.tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            pretty_xml = reparsed.toprettyxml(indent="  ")

            with open(xml_file, "w", encoding="utf-8") as out:
                out.write(pretty_xml)

            print(f"[✓] Exported XML to {xml_file}")

    except Exception as e:
        print(f"[!] Failed to export XML: {e}")