import cv2
import numpy as np
from ultralytics import YOLO

class ParkingAssistantModel:
    def __init__(self, model_variant='yolov8n'):
        # Wir nutzen ein vortrainiertes YOLOv8n (nano) Modell,
        # das schnell ist und gut auf Streamlit läuft.
        self.model = YOLO(model_variant)

    def analyze_image(self, image):
        """
        Analysiert ein Bild und gibt simulierte Lückengrößen zurück.
        
        Hier wird eine echte KI (YOLOv8) genutzt, um Autos zu erkennen.
        Eine echte Lückenmessung ist komplex und erfordert Tiefenkameras
        oder photogrammetrische Referenzen. Für das Projekt
        simulieren wir die Lückengröße basierend auf der Anzahl der
        erkannten Autos.
        """
        results = self.model(image)
        
        num_cars = 0
        for r in results:
            for c in r.boxes.cls:
                if int(c) == 2:  # Klasse 2 ist standardmäßig 'car' in YOLO
                    num_cars += 1
        
        # Simuliere die Lückengröße basierend auf der Anzahl der Autos
        if num_cars >= 2:
            gap_size = np.random.uniform(5.0, 5.6)  # Eher größere Lücke
        elif num_cars == 1:
            gap_size = np.random.uniform(3.5, 4.3)  # Knappere Lücke
        else:
            gap_size = np.random.uniform(2.5, 3.2)  # Zu klein

        # Annotiere das Bild für das Layout (Zeichne Boxen um erkannte Autos)
        # Für das Projekt simulieren wir hier eine einfache Anzeige
        annotated_image = results[0].plot()
        
        return gap_size, annotated_image, num_cars

def get_parking_assistant_model():
    # Factory-Methode, um das Modell als Singleton-artiges Objekt zu halten
    return ParkingAssistantModel()
