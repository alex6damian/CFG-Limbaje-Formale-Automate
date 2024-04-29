def load_file(file_name): #extrage informatia din fisier
    with open(file_name, 'r') as file: #deschidere fisier
        continut=[] #initializare lista
        for lines in file: #parcurgere linii
            lines=lines.strip() #eliminare spatii
            if '#' in lines: #eliminare comentarii
                continue
            else:
                continut.append(lines) #adaugare linie in lista
        return continut #returnare lista

def get_section_list(content): #separa datele
    sections={} #initializare dictionar
    elements=[] #initializare lista
    name='a' #initializare nume
    #parcurgere fisier
    for lines in content:
        if lines[-1]==":": #verificare daca linia contine :
            lines = lines[:len(lines) - 1] #eliminare :
            name = lines.strip() #eliminare spatii
            elements = []
        #citire pana la stop
        elif lines!='Stop': #verificare daca linia contine Stop
            lines=lines.split(",") #separare elemente
            lines=[item.strip() for item in lines] #eliminare spatii
            if name=="Vars": #verificare daca numele sectiei este Vars
                if "*" in lines: #verificare daca * se afla in lista
                    sections["*"]=lines[0]  #adaugare element in dictionar
                elements.append(lines[0]) #adaugare element in lista
            elif name=="Sigma": #verificare daca numele sectiei este Sigma
                elements.append(lines[0]) #adaugare element in lista
            elif name=="Rules": #verificare daca numele sectiei este Rules
                elements.append((lines[0], lines[1:])) #adaugare element in lista
        elif lines=='Stop': #adaugare elemente in dictionar
            sections[name]=elements #completez dictionarul
    return sections #returnare dictionar

def get_section_content(content, section_name): #obtinere valori ale unei sectii
    return content[section_name] #returnare valori
