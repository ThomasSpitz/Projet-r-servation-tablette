import os as os
import csv
os.chdir('/home/Thomas/Documents/Projets perso/Projet NSI HTML/')                                          #changement du répertoire courant


def generation_fichier_csv():
    f=open('DemandeEleve.csv','w')                                                        #Création du fichier csv
    f.close()

    Titres=['Date','Heure','Duree de reservation','Nom eleve tablette','Nombre de tablettes reservees']                   #Titres des colonnes
   
    with open('DemandeEleve.csv',"w")as sortie:                                           #Insertion dans le fichier des colonnes
        TitresColonnes=csv.DictWriter(sortie,Titres)
        TitresColonnes.writeheader()    

def generation_fichier_CSS():
    f=open('CSS_Site.css','w')                                                          #Création du fichier CSS
    f.writelines('*{font-family:Century Gothic; }\n')                                   #On définie la m^me police pour toute la page
    f.writelines('\nh1 { text-align: center;\n')
    f.writelines('    font-weight:bold;\n')                                             #On définie la police, la taille, la couleur ... du titre de la page
    f.writelines('    color:#557bad;\n')
    f.writelines('    font-size: 3em;\n')
    f.writelines('    }\n')
    f.writelines('\nh2 { text-align: center;\n')
    f.writelines('    color:#ffffff;\n')
    f.writelines('    }\n')
    f.writelines('\ntable  {table-layout: fixed;\n')
    f.writelines('    width:50em;\n')                                             #On définie le style des tableaux(taille, couleur et taille de la bordure, 
    f.writelines('    height:15em ;\n')                                                 #fond) ainsi que l'emplacement des écritures
    f.writelines('    text-align:center;\n')
    f.writelines('    vertical-align:center;\n')
    f.writelines('    border-collapse: collapse;\n')    
    f.writelines('    border:3pt black;\n')
    f.writelines('    border:3pt solid #425c66;\n')
    f.writelines('    background:#ebf9ff;}')
    
def convertir_le_fichier(fichier):                                          
    f=open(fichier,encoding="utf8")                                                     #On convertie un fichier(csv) en tableau ded dictionnaires.
    DemandeEleve=list(csv.DictReader(f, delimiter=","))
    return DemandeEleve


def ecriture(t):                                                                        #Fonction regroupant toutes les fonctions chargées de créer la page html
    f=open("projet.html", "w")    
    tetedepage(t,f)
    tableaurecapitulatif(t,f)
    creationplanning(t,tableauplanning(t),f)
    

def tetedepage(t,f):                                                                    #Fonction qui écrit le début de la page html, contenant la tete de page mais aussi le titre et le fond d'ecran de la page.
    f.writelines("<!DOCTYPE html> \n")
    f.writelines("<html> \n")
    f.writelines("<head> \n")
    f.writelines("    <meta charset='UTF-8' /> \n")
    f.writelines("    <meta name='description' content='Reservation tablette' /> \n")              
    f.writelines("    <meta name='keywords' content='HTML5,CSS3,JavaScript,PHP' /> \n")
    f.writelines("    <meta name='author' content='Thomas et Mathieu' /> \n")
    f.writelines('<link href="CSS_Site.css" type="text/css" rel="stylesheet"/>\n')
    f.writelines(" <title>\n  Reservation tablette\n </title> \n")
    f.writelines("</head> \n")
    f.writelines('<body background="Arriere plan2.jpg"> \n')
    f.writelines('<h1 align=center> Reservation tablette </h1>\n')            
    f.writelines('<link href="CSS_Site.css" type="text/css" rel="stylesheet"/>\n')

def tableaurecapitulatif(t,f):                                                          #Fonction qui utilise le tableau recapitulatif pour l'écrire dans la page html.
    f.writelines("<h2>Tableau recapitulatif des demandes</h2>\n")
    f.writelines("<table align=center border='1'>\n")                                   #Créarion des colonnes
    f.write("<tr>\n")                                                       
    f.write(f"<td>Date</td>\n")
    f.write(f"<td>Heure</td>\n")                                            
    f.write(f"<td>Duree de reservation</td>\n")
    f.write(f"<td>Nom eleve tablette</td>\n")
    f.write(f"<td>Nombre de tablettes reservees</td>\n")
    f.write("</tr>\n")
    for i in range (len(t)):                                                            #Insertion, à l'aide d'une boucle for, du tableau de dictionnaire dans un tableau sur la page html
        f.write("<tr>\n")
        f.write(f"<td>{t[i]['Date']}</td>\n")
        f.write(f"<td>{t[i]['Heure']}</td>\n")
        f.write(f"<td>{t[i]['Duree de reservation']}</td>\n")
        f.write(f"<td>{t[i]['Nom eleve tablette']}</td>\n")
        f.write(f"<td>{t[i]['Nombre de tablettes reservees']}</td>\n")
        f.write("</tr>\n")
    f.write("</table>\n")

def tableauplanning(t):                                                                 #Création du planning de réservation qui prend pour l'instant la forme d'un tableau bidimensionnel.
    Jourdelasemaine=['Lundi','Mardi','Mercredi','Jeudi','Vendredi']                     #Tableau contenant les jours de la semaine dans l'ordre
    Horairelycee=['8h10 - 9h10','9h10 - 10h10','10h20 - 11h20','11h20 - 12h20','12h20 - 13h20','13h20 - 14h20','14h20 - 15h20','15h30 - 16h30','16h30 - 17h30','17h30 - 18h30']
    Planning=[]
    for i in Horairelycee:                                                               #On créé, à l'aide d'une boucle for, un planning avec les heures (à gauche) et des zéros dans toutes les cases.
        Planning.append([i,0,0,0,0,0])
    for i in Horairelycee:                                                               #On parcours les deuc tableaux avec deux boucles for
        for j in range(len(t)):
            if str(i)==str(t[j]['Heure']):                                              #Si une ligne du tableau récapitulatif a une heure égale à une heure du planning, on ajoute dans le tableau bidimensionnel
                
                Planning[convert_heure(i)][convert_jour(t[j]['Date'])]+=int(t[j]['Nombre de tablettes reservees'])                            #à la bonne ligne en fonction de l'heure que l'on a déterminé au dessus(1ereligne correspond à 8 heures donc on enlève 8),
    return Planning                                                                     #puis à la bonne colonne grace à une fonction qui permet de transformer le jour souhaité en sa position dans le tableau
                                                                                        #On ajoute enfin 1 dans cette case pour signifier qu'il y a une une réservation à cet horaire

def creationplanning(t,Planning,f):                                                     #Fonction qui écrit le tableau ci dessus dans un fichier html.
    f.write('<br> ')                                                                    #On saute des lignes entre les deux tableaux
    f.write('<br> ')
    f.write('<br> ')
    f.writelines("<h2>Planning de reservation avec le nombre de tablettes restantes </h2>\n")
    f.writelines("<table align=center border='1'>\n")                                   #On créé le tableau
    f.write("<tr>\n")
    f.write(f"<td>    </td>\n")                                                         #On créé les colonnes(composés de jour de la semaine)
    f.write(f"<td>Lundi</td>\n")
    f.write(f"<td>Mardi</td>\n")                                            
    f.write(f"<td>Mercredi</td>\n")
    f.write(f"<td>Jeudi</td>\n")
    f.write(f"<td>Vendredi</td>\n")
    f.write("</tr>\n")

    for i in range (len(Planning)):                                                     #On parcourt le tableau bidimensionnel "Planning" à l'aide de deux boucles for 
        f.write("<tr>\n")
        for j in range(6):
            if j==0:
                f.write(f"<td>{Planning[i][j]}</td>\n")
            elif Planning[i][j]>=70:                                                       #Si le nombres de réservation sur une case est supérieur à 70, le fond de la case sera rouge
                f.write(f"<td bgcolor='red'>Plus de tablette disponible !</td>\n")                   #Sinon on insère normalement le nombre de réservation
            else :
                f.write(f"<td>{70-Planning[i][j]}</td>\n")                              #On soustrait le nombre de tablettes total au nombre de tablettes réservé.

        
        f.write("</tr>\n")                                                              #On termine le tableau puis la page html
    f.write("</table>\n")
    
    f.writelines("</body> \n")
    f.writelines("</html> \n")
    f.close()

def convert_jour(date):                                                                 #Fonction qui convertit les jours de la semaine en chiffre qui désigne leur ordre(ex: Lundi-> 1, Vendredi->5)
    Jourdelasemaine=['Lundi','Mardi','Mercredi','Jeudi','Vendredi']                     #Tableau contenant les jours de la semaine dans l'ordre
    for i in range(len(Jourdelasemaine)):                                               #On parcours le tableau avec une boucle for
        if Jourdelasemaine[i]==date:                                                    #Si la date en entrée est égale à la case de Jourdelasemaine d'indice i, on retourne i+1 car on veut que Lundi corresponde à 1 et non 0 :)   
            return i+1

def convert_heure(heure):
    Horairelycee=['8h10 - 9h10','9h10 - 10h10','10h20 - 11h20','11h20 - 12h20','12h20 - 13h20','13h20 - 14h20','14h20 - 15h20','15h30 - 16h30','16h30 - 17h30','17h30 - 18h30']
    for i in range(len(Horairelycee)):                                               #On parcours le tableau avec une boucle for
        if Horairelycee[i]==heure:                                                    #Si la date en entrée est égale à la case de Jourdelasemaine d'indice i, on retourne i+1 car on veut que Lundi corresponde à 1 et non 0 :)   
            return i+1

try :
    ecriture(convertir_le_fichier('DemandeEleve.csv'))                                      #Script éxécutant la fonction écriture avec en entrée le fichier CSV convertie en tableau de dictionnaire.
except :
    generation_fichier_csv()
    generation_fichier_CSS()
    ecriture(convertir_le_fichier('DemandeEleve.csv'))     
    
