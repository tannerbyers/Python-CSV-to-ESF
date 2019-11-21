import csv
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from lxml import etree
from xml.dom import minidom



def Runprogram():
    with open('EditsinCSV.csv') as ValuesToAddFile, open('result.esf', 'r+')as testxml:
        ValuesToAddFileList = list(csv.reader(ValuesToAddFile, delimiter=','))

        root=Element('SeverityConfigFile')
        root.set('Version', "2.0")
        root.set('Mode', "override")
        root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        root.set('xsi:noNamespaceSchemaLocation', "SeverityConfig.xsd")
        tree = ElementTree(root)
        SeverityDefinition = Element('SeverityDefinition')
        root.append(SeverityDefinition)
        SeverityUsage = Element('SeverityUsage')
        root.append(SeverityUsage)
        for row in ValuesToAddFileList:
            if (row[0] == "EDIFECS Edit"):
                print(row)
            else:
                # print(row[0])
                ApplyTo=Element('ApplyTo')
                SeverityUsage.append(ApplyTo)
                criteria=Element('Criteria')
                ApplyTo.append(criteria)
                criteria.set('Name','emp.snip')
                criteria.set('Value', row[1])
                criteria2=Element('Criteria')
                ApplyTo.append(criteria2)
                criteria2.set('Name', 'emp.id')
                criteria2.set( 'Value', row[0])
                setSeverity=Element('SetSeverity') 
                ApplyTo.append(setSeverity)  
                setSeverity.set('SeverityID', "1001")
        # tree.write(testxml)
        test = (prettify(root))
        print(tree)
        testxml.write(test)

        

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8',method="xml")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")


Runprogram()