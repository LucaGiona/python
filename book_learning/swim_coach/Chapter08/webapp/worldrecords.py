import ssl
import gazpacho

# SSL-Verifizierung global deaktivieren
ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
html = gazpacho.get(URL)
print(f"Länge des HTML: {len(html)} Zeichen")
