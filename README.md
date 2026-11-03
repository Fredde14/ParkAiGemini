# 🚗 KI Parkassistent (Informatikprojekt)

Willkommen beim KI-Parkassistenten, einem fortgeschrittenen Informatikprojekt, das Deep Learning nutzt, um dir beim Einparken zu helfen.

Diese App analysiert ein Foto deiner Parklücke, nutzt ein vortrainiertes Objekterkennungsmodell (**YOLOv8**) und simuliert den Einparkprozess basierend auf deinen Fahrzeugmaßen.

## Features

* **Vortrainiertes KI-Modell:** Nutzt YOLOv8 von Ultralytics, um Autos in Bildern zu erkennen.
* **Streamlit Oberfläche:** Eine moderne Web-App, die das Layout eines echten Parkassistenten nachahmt.
* **Simulierte Lückenmessung:** Berechnet eine simulierte Lückengröße basierend auf KI-Analysen.
* **Szenario-Simulation:** Prüft, ob dein Auto in die Lücke passt und gibt einen Einpark-Guide.

## Installation & Start

1. Repository klonen oder herunterladen.
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
