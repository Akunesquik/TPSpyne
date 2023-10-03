import os

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Chemin du dossier à surveiller
folder_to_watch = "depot/"

# Commande pour exécuter le client.py
client_command = "python client.py"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif event.src_path.endswith(".txt"):
            print(f"Fichier créé: {event.src_path}")
            # Exécuter le client.py avec le fichier comme argument
            
            os.system(f"{client_command} {event.src_path}")

if __name__ == "__main__":
    print("Listener Allumé")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
