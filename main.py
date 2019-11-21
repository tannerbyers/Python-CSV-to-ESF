import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.dom import minidom



def Runprogram():
    with open('EditsinCSV.csv') as ValuesToAddFile, open('result.esf', 'r+')as testxml:
        ValuesToAddFileList = list(csv.reader(ValuesToAddFile, delimiter=','))

        root=Element('SeverityConfigFile')
        root.set('Version', "2.0")
        root.set('Mode', "override")
        root.set('xmlns:xsi', "http://www.w3.org/2001/XMLSchema-instance")
        root.set('xsi:noNamespaceSchemaLocation', "SeverityConfig.xsd")
        SeverityDefinition = Element('SeverityDefinition')
        root.append(SeverityDefinition)
        SeverityUsage = Element('SeverityUsage')
        root.append(SeverityUsage)


        def ErrorXMLGenerator(ErrorCode, SnipLvl):
            ApplyTo=Element('ApplyTo')
            SeverityUsage.append(ApplyTo)
            criteria=Element('Criteria')
            ApplyTo.append(criteria)
            criteria.set('Name','emp.snip')
            criteria.set('Value',SnipLvl)
            criteria2=Element('Criteria')
            ApplyTo.append(criteria2)
            criteria2.set('Name', 'emp.id')
            criteria2.set( 'Value', ErrorCode)
            setSeverity=Element('SetSeverity') 
            ApplyTo.append(setSeverity)  
            setSeverity.set('SeverityID', "1001")

        for row in ValuesToAddFileList:
            if (row[0] == "EDIFECS Edit"):
                print(row)
            else:
                ErrorXMLGenerator(row[0], row[1])
        
        prettyXMLdata = (prettify(root))
        print(prettyXMLdata)
        testxml.write(prettyXMLdata)

        

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8',method="xml")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")





Runprogram()