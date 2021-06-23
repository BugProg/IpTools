import requests
import os
from os import system
from colorama import Fore, init

init()

chemin_txt = (__file__ + "/../config.txt")


def clear():
    system("cls")


def error(message):
    print(Fore.RESET + "[" + Fore.RED + "ERROR" + Fore.RESET + "]", message)


def init_page():
    system("title ip")
    system("mode 160, 40")


def ip_recup():
    # API permettant de recuperer son adresse IP v4
    url_ip = "https://api.ipify.org"

    reponse = requests.get(url_ip)
    ip_client = reponse.text

    return (ip_client)


def ip_info(ip, key):
    url_infoip = f"http://api.ipstack.com/{ip}?access_key={key}"

    reponse = requests.get(url_infoip)
    content = reponse.json()
    return content


def config_api(id_api):
    configuration = open(chemin_txt, "w")
    configuration.write(id_api)
    configuration.close()


def config():
    clear()
    print(Fore.CYAN + """


    
    
        

                                                       d8b               888                     888          
                                                       Y8P               888                     888          
                                                                       888                     888          
                                                       888 88888b.       888888 .d88b.   .d88b.  888 .d8888b  
                                                       888 888 "88b      888   d88""88b d88""88b 888 88K      
                                                       888 888  888      888   888  888 888  888 888 "Y8888b. 
                                                       888 888 d88P      Y88b. Y88..88P Y88..88P 888      X88 
                                                       888 88888P"        "Y888 "Y88P"   "Y88P"  888  88888P' 
                                                           888                                                
                                                           888                                                
                                                           888                            
                                                        ___________________________________________________                
                                                        
                                                            [1] Clé       [2] Langues        [b] Retour 
                                                        ___________________________________________________                                                           
                                                                                                                                                    
    """ + Fore.RESET)
    config_menu_choice = input(Fore.CYAN + """                                                        [>] Config : """)
    if int(config_menu_choice) == 1:
        config_key = input(Fore.CYAN + """                                                        [>] Clé : """)

        config_txt = open(chemin_txt, "w")
        config_txt.write(config_key)
        config_txt.close()

    elif int(config_menu_choice) == 1:
        print("🚧 En development")
    elif config_menu_choice == "b":
        main()


def myip():
    clear()
    look = open(chemin_txt, "r")
    key = (look.readlines())[0]
    look.close()

    ip = ip_recup()
    info = ip_info(ip, key)
    city = info["city"]
    country = info["country_name"]
    space = (38 - 8 - len(city))
    space2 = (12 - len(country))
    vp = (Fore.YELLOW + "        " + city + (space * " ") + country + (space2 * " ") + Fore.CYAN)
    print(Fore.CYAN + """


    
    
        

                                                       d8b               888                     888          
                                                       Y8P               888                     888          
                                                                       888                     888          
                                                       888 88888b.       888888 .d88b.   .d88b.  888 .d8888b  
                                                       888 888 "88b      888   d88""88b d88""88b 888 88K      
                                                       888 888  888      888   888  888 888  888 888 "Y8888b. 
                                                       888 888 d88P      Y88b. Y88..88P Y88..88P 888      X88 
                                                       888 88888P"        "Y888 "Y88P"   "Y88P"  888  88888P' 
                                                           888                                                
                                                           888                                                
                                                           888                            

                                                        ╔══════════════════════════════════════════════════╗
                                                        ║                   """ + Fore.YELLOW + ip + Fore.CYAN + """                  ║ 
                                                        ║        Ville                         Pays        ║ 
                                                        ║""" + vp + """║
                                                        ╚══════════════════════════════════════════════════╝        
    """ + Fore.RESET)


def main():
    print(Fore.CYAN + """


    
    
        

                                                       d8b               888                     888          
                                                       Y8P               888                     888          
                                                                       888                     888          
                                                       888 88888b.       888888 .d88b.   .d88b.  888 .d8888b  
                                                       888 888 "88b      888   d88""88b d88""88b 888 88K      
                                                       888 888  888      888   888  888 888  888 888 "Y8888b. 
                                                       888 888 d88P      Y88b. Y88..88P Y88..88P 888      X88 
                                                       888 88888P"        "Y888 "Y88P"   "Y88P"  888  88888P' 
                                                           888                                                
                                                           888                                                
                                                           888                            
                                                        ___________________________________________________                
                                                        
                                                          [1] MonIP       [2] LocaliserIP       [3] Config  

                                                          [4] A propos    [!] Coming Soon
                                                        ___________________________________________________                                                           
                                                                                                                                                    
    """ + Fore.RESET)
    main_menu_choice = input(Fore.CYAN + """                                                        [>] Menu : """)
    if int(main_menu_choice) == 1:
        look = open(chemin_txt, "r")
        text = look.readlines()
        look.close()

        if text == []:
            error("Aucune clé pour l'api n'a été configuré")
        elif len(text) > 1:
            error("La clé à été mal configuré :/")
        elif len(text[0]) != 32:
            error("La clé à été mal configuré :/")
        else:
            myip()

    elif int(main_menu_choice) == 2:
        print("ok")
    elif int(main_menu_choice) == 3:
        config()
    elif int(main_menu_choice) == 4:
        print("ok")
    else:
        print("NON")


init_page()

clear()
main()
