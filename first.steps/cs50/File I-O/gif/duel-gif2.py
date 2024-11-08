import sys
from PIL import Image

images = []

# Lade die Bilder aus den Argumenten
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Überprüfen, ob mindestens zwei Bilder geladen wurden
if len(images) > 1:
    # Sequenz für den Switch-Effekt: Bild 1, Bild 2, dann zurück zu Bild 1
    switch_frames = [images[0], images[1], images[0]]
    
    # Speichere das animierte GIF
    switch_frames[0].save(
        "amaro-switch.gif",
        save_all=True,
        append_images=switch_frames[1:],  # Restliche Frames hinzufügen
        duration=[250, 250, 2500],      # Zeit pro Frame: 2,5 Sek. für jeden Frame
        loop=5                            # Animation läuft 5 Mal
    )
    print("GIF saved as amaro-switch.gif")
else:
    print("Please provide at least two images for the switch effect.")
