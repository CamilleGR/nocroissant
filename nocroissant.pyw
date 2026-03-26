#!python
import os, sys, signal
import cv2
import ctypes
import keyboard
import time 
from datetime import datetime

ALREADY_TRIGGERED=False

#
#  _  _  ___   ___ ___  ___ ___ ___ ___   _   _  _ _____ 
# | \| |/ _ \ / __| _ \/ _ \_ _/ __/ __| /_\ | \| |_   _|
# | .` | (_) | (__|   / (_) | |\__ \__ \/ _ \| .` | | |  
# |_|\_|\___/ \___|_|_\\___/___|___/___/_/ \_\_|\_| |_|  
#                                                        
#   Protection anti-croissantage : 
#   - Ecoute le clavier 
#   - En cas de saisie, prend une photo et l'enregistre 
#   - En cas de saisie : lock de la session
#


def print_banner() : 

    banner = """  
 _  _  ___   ___ ___  ___ ___ ___ ___   _   _  _ _____ 
 | \\| |/ _ \\ / __| _ \\/ _ \\_ _/ __/ __| /_\\ | \\| |_   _|
 | .` | (_) | (__|   / (_) | |\\__ \\__ \\/ _ \\| .` | | |  
 |_|\\_|\\___/ \\___|_|_\\\\___/___|___/___/_/ \\_\\_|\\_| |_|  
                                                        
  PROTECTION ANTI-CROISSANTAGE ACTIVE

    """
    print(banner)


def signal_handler(signal, frame):
    handler_croissantage()
    #print('PROTECTION DESACTIVE')
    #print('FIN DU PROGRAMME')
    

signal.signal(signal.SIGINT, signal_handler)
# Prend une photo avec la caméra frontale
def take_photo(output, quiet=True):
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        if not quiet: cv2.imshow("Captured", frame)
        cv2.setWindowProperty("Captured", cv2.WND_PROP_TOPMOST, 1)
        cv2.imwrite(output, frame)  
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
                    
    else:
        print("Failed to capture image.")
    cam.release() 

# Déclenche une pop up
def popup(name, message) :
    ctypes.windll.user32.MessageBoxW(0, message, name, 0)

def lock_session():
    # Utilise l'API Windows pour verrouiller la session
    ctypes.windll.user32.LockWorkStation()


#
#   HANDLER : fonction appelée lors d'une détection
#

def handler_croissantage() : 
    dateStr= datetime.today().strftime('%Y%m%d%H%M%S')
    dossier_du_script = os.path.dirname(os.path.abspath(sys.argv[0]))
    take_photo(output=f"{dossier_du_script}\photo_"+dateStr+".png",quiet=False)
    #popup("Avertissement", "Bye !")
    lock_session()
    sys.exit(0)




def capture_keyboard_events():
    events = []
    def on_key_press(event):
        global ALREADY_TRIGGERED
        events.append(event.name)
        if event.name == 'esc':
            return False  # Arrête la capture si la touche ESC est pressée
        elif not ALREADY_TRIGGERED : 
            handler_croissantage()
            ALREADY_TRIGGERED = True
    keyboard.on_press(on_key_press)
    # Attend que l'utilisateur appuie sur ESC pour arrêter la capture
    keyboard.wait('esc')
    return events



if __name__ == "__main__" :   
    print_banner()  
    events = capture_keyboard_events()
    for i,e in enumerate(events):
        if e == "space" : 
            events[i] = " "
    
    print("".join(events))

