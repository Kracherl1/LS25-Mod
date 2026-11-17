import os
import zipfile

# Name der finalen ZIP-Datei
output_filename = "FS25_test.zip"

# Zu ausschließende Ordner und Dateien
excluded_dirs = {".idea"}
excluded_files = {"test_export_log.txt", output_filename, "zipper.py", "zipper.bat"}

with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk("."):
        # Verzeichnisse herausfiltern, damit os.walk gar nicht erst in .idea hineingeht
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:
            if file in excluded_files:
                continue

            file_path = os.path.join(root, file)
            # Relativer Pfad, damit die Ordnerstruktur im Archiv sauber bleibt
            arcname = os.path.relpath(file_path, ".")
            zipf.write(file_path, arcname)

print(f"Fertig! Alles wurde in '{output_filename}' gezippt.")

# Verhindert das sofortige Schließen des Fensters
input("Drücke Enter, um das Programm zu beenden...")