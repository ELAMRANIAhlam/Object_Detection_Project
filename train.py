from ultralytics import YOLO

# Charger un modèle
model = YOLO("yolov8n.yaml")  # Construire un nouveau modèle à partir de zéro

# Utiliser le modèle
results = model.train(data="config.yaml", epochs=1)  # Entraîner le modèle






















