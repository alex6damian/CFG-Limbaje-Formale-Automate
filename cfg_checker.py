import cfg_passer

def validation(content):

    #verificare lungime alfabet
    if len(content['Vars'])<1:
        return False
    if len(content['Sigma'])<1:
        return False

    #verificare unicitate aparitii simbol in alfabet
    if sorted(content['Sigma'])!=sorted(list(set(content['Sigma']))):
        return False

    #verificare unicitate aparitii stari
    if sorted(content['Vars']) != sorted(list(set(content['Vars']))):
        return False

    #verificare corectitudine tranzitii
    for elements in content['Rules']:
        if elements[0] not in content['Vars']:
            return False
        elif len(elements)!=2:
            return False
        for item in elements[1]:
            if item not in content['Vars'] and item not in content['Sigma']:
                return False


    #verificare daca avem stare initiala
    if not content['*']:
        return False

    if "," in content['*']:
        return False

    return True

def main():
    file = cfg_passer.load_file("cfg_input") # importam fisierul
    section = cfg_passer.get_section_list(file) # extragem sectiunile

if "__name__"=="__main__": # daca rulam acest fisier
    main() # rulam functia main
