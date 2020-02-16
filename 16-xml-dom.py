import xml.dom.minidom

def main():
    # Parse XML file
    doc = xml.dom.minidom.parse("samplexml.xml")

    # Print out the document node and the name of the first child tag
    print (doc.nodeName)
    print (doc.firstChild.tagName)

    # Get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print ("%d skills:" % skills.length)
    for skill in skills:
        print (skill.getAttribute("name"))

    # Create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print ("%d skills:" % skills.length)
    for skill in skills:
        print (skill.getAttribute("name"))

        
if __name__ == "__main__":
    main()

