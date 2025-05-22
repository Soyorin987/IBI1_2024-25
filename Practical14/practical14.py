#Function: to parse an XML file that contains Gene Ontology terms,this process will be done twice using sax and dom
import xml.sax
import xml.dom.minidom #import needed libraries
import time #to measure the time taken for the process

infile= r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical14\go_obo.xml'
start_time= time.time()#start the time
DOMTree = xml.dom.minidom.parse(infile)#input the file and start to parse it
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")#extract the term elements

#create a dictionary to store the information
DOM_info = {
    "biological_process": {"id": "", "count": 0},
    "molecular_function": {"id": "", "count": 0},
    "cellular_component": {"id": "", "count": 0}
}

#deal with the extracted term elements
for term in terms:
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue #extract the id
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue #extract the namespace
    is_a_list = term.getElementsByTagName("is_a") #extract the is_a elements
    is_a_count = len(is_a_list) #count the number of is_a elements

if namespace in DOM_info and is_a_count > DOM_info[namespace]["count"]:
        DOM_info[namespace]["id"] = term_id
        DOM_info[namespace]["count"] = is_a_count
#check if the namespace is in the dictionary and if the count is greater than the current count,then update the dictionary

end_time = time.time()#end the time
time1= end_time - start_time#calculate the time taken for the process

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.current_id = ""
        self.current_namespace = ""
        self.is_a_count = 0
        self.max_info = {
            "biological_process": {"id": "", "count": 0},
            "molecular_function": {"id": "", "count": 0},
            "cellular_component": {"id": "", "count": 0}
        }

    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "term":
            # reset all values for a new <term>
            self.current_id = ""
            self.current_namespace = ""
            self.is_a_count = 0

    def characters(self, content):
        if self.current_data == "id":
            self.current_id += content.strip()
        elif self.current_data == "namespace":
            self.current_namespace += content.strip()
        elif self.current_data == "is_a":
            self.is_a_count += 1  # every time a <is_a> text appears, we count 1

    def endElement(self, tag):
        if tag == "term":
            if self.current_namespace in self.max_info:
                if self.is_a_count > self.max_info[self.current_namespace]["count"]:
                    self.max_info[self.current_namespace]["count"] = self.is_a_count
                    self.max_info[self.current_namespace]["id"] = self.current_id
        self.current_data = ""  # reset current_data

start_time2 = time.time()#start the time
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

handler = GOHandler()
parser.setContentHandler(handler)
parser.parse(infile)
end_time2 = time.time()#end the time
time2= end_time2 - start_time2

timedifference = time1 - time2 #calculate the time difference between the two methods

#output the result
for ns, info in handler.max_info.items():
    print(f"{ns}: Max is_a count = {info['count']}, GO term ID = {info['id']}")

print("Using Dom costs", time1, "seconds","Using SAX costs", time2, "seconds","and the time difference is", timedifference, "seconds")#output the time taken for the process

#DOM was faster than SAX by approximately 11.65 seconds