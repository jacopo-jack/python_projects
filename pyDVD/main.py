#import area
import os
import webbrowser 

# Funzione principale
def choice():
 while True:
    print("PyDVD_Manager")
    print("1. Ripping")
    print("2. Crea DVD")
    main_choice = input("Inserisci la tua scelta: ")

    if main_choice == "1":
        ripper_to_use()
    elif main_choice == "2":
        authoring_area()
    else:
        print("Scelta non valida. Riprova.")
        choice()

# Funzione di scelta del ripper
def ripper_to_use():
    print("DVD Ripper Chooser")
    print("Scegli il tuo sistema operativo:")
    choice = input("Inserisci 'Windows', 'Mac', o 'Linux': ").strip().lower()

    if choice == "windows":
        open_webpage("https://www.google.com/search?q=windows+dvd+rippers")
    elif choice == "mac":
        open_webpage("https://www.google.com/search?q=mac+dvd+rippers")
    elif choice == "linux":
        open_webpage("https://www.google.com/search?q=linux+dvd+rippers")
    else:
        print("Sistema operativo non riconosciuto. Riprova.")
        ripper_to_use()

# Funzione per aprire una pagina web
def open_webpage(url):
    webbrowser.open(url)

# Funzione di authoring
def authoring_area():
    print("PyDVD_Manager")
    print("Se vuoi creare un DVD video digita 'DVD', altrimenti 'Hybrid'")
    choice = input("Dimmi ciò che vuoi fare: ")

    if choice == "DVD":
        dvd()
    elif choice == "Hybrid":
        hybrid()
    else:
        print("Scelta non valida. Riprova.")
        authoring_area()

# Funzione per creare ambiente DVD
def dvd():
    print("Creazione ambiente DVD in corso")
    create_directory('dvd_project')
    
    # Spostarsi nella cartella 'dvd_project'
    os.chdir('dvd_project')
    print(f"Directory corrente: {os.getcwd()}")  # Stampa la directory corrente
    
    # Creazione delle sotto-cartelle e dei file
    create_directory('ui')  # Crea la cartella ui
    create_file('ui/ui.html', '<html>\n<head>\n<title>UI</title>\n</head>\n<body>\n</body>\n</html>')  # Crea ui.html
    
    create_directory('style')  # Crea la cartella style
    create_file('style/style.css', 'body {\n    font-family: Arial, sans-serif;\n}')  # Crea style.css
    
    create_directory('video')  # Crea la cartella video vuota

# Funzione per creare ambiente Hybrid
def hybrid():
    print("Creazione ambiente Hybrid in corso")
    create_directory('hybrid_project')
    
    os.chdir('hybrid_project')
    print(f"Directory corrente: {os.getcwd()}")  # Stampa la directory corrente
    
    # Creazione delle sotto-cartelle e dei file
    create_directory('ui')  # Crea la cartella ui
    create_file('ui/ui.html', '<html>\n<head>\n<title>UI</title>\n</head>\n<body>\n</body>\n</html>')  # Crea ui.html
    
    create_directory('style')  # Crea la cartella style
    create_file('style/style.css', 'body {\n    font-family: Arial, sans-serif;\n}')  # Crea style.css
    
    create_directory('video')  # Crea la cartella video vuota
    create_directory('app') 
    create_directory('script')


# Funzione per creare una directory
def create_directory(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    print(f"Cartella '{folder_name}' creata")

# Funzione per creare un file con contenuto
def create_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' creato con successo")

# Avvia il programma
choice()
