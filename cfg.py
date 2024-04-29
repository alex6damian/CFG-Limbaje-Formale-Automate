import cfg_passer # importam modulul cfg_passer
from random import randint # importam functia randint
import cfg_checker # importam modulul cfg_checker

def transformare(string, variabile, rules):
    for element in string: # parcurgem stringul
        if element in variabile: # daca elementul este o variabila
            for rule in rules: # parcurgem regulile
                if rule[0]==element: # daca regula este pentru variabila curenta
                    nr=randint(0, len(rules)-1) # alegem o regula random
                    x=[rules[nr][1][i] for i in range(len(rules[nr][1]))] # construim stringul
                    string[string.index(element):string.index(element)+1]=x # inlocuim variabila cu stringul
                    break # trecem la urmatorul element

    for element in string: # parcurgem stringul
        if element in variabile: # daca elementul este o variabila
            string=transformare(string, variabile, rules) # aplicam functia pe string

    return string # returnam stringul

def main():

    c=cfg_passer.load_file("cfg_input") # importam fisierul

    s=cfg_passer.get_section_list(c) # extragem sectiunile

    variabile=cfg_passer.get_section_content(s, "Vars") # variabile

    sigma=cfg_passer.get_section_content(s, "Sigma") # alfabet

    rules=cfg_passer.get_section_content(s, "Rules") # reguli

    curent=[cfg_passer.get_section_content(s, "*")] # variabila de start

    final=transformare(curent, variabile, rules) # aplicam functia de transformare

    print("".join(final)) # afisam rezultatul



if __name__ == "__main__": # daca rulam acest fisier
    if(cfg_checker.validation(cfg_passer.get_section_list(cfg_passer.load_file("cfg_input")))==True): # daca CFG-ul este valid
        print("CFG Valid") # afisam daca CFG-ul este valid
        main() # rulam functia main
    else:
        print("CFG Invalid") # afisam daca CFG-ul este invalid