# =====================================================================
# PLANTILLA GENÉRICA: Clasificación Biclase con Imágenes de Google Drive
# =====================================================================

# ---------------------------------------------------------------------
# PASO 1: Conectar a Google Drive
# ---------------------------------------------------------------------
from google.colab import drive
drive.mount('/content/drive')

# ---------------------------------------------------------------------
# PASO 2: Importar Librerías Universales
# ---------------------------------------------------------------------
import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# Configuración automática de Hardware (GPU si está activa, si no CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Trabajando con el dispositivo: {device}\n")

# ---------------------------------------------------------------------
# PASO 3: Configurar Rutas del Dataset (¡MODIFICA AQUÍ!)
# ---------------------------------------------------------------------
# Si tu carpeta principal en Drive se llama diferente a "CNN", cambia el nombre aquí.
RUTA_TRAIN = '/content/drive/MyDrive/CNN/TRAIN/'
RUTA_TEST = '/content/drive/MyDrive/CNN/TEST/'

# ---------------------------------------------------------------------
# PASO 4: Transformaciones de Imágenes (Data Augmentation)
# ---------------------------------------------------------------------
# Nota didáctica: ResNet, VGG y la mayoría de redes comerciales esperan 224x224.
# Si tus imágenes son muy grandes o muy chicas, aquí controlas su entrada a la red.
transformaciones_train = transforms.Compose([
    transforms.Resize((224, 224)),           # Redimensionar todas las imágenes al mismo tamaño
    transforms.RandomHorizontalFlip(),       # Volteo aleatorio (Data Augmentation opcional)
    transforms.ToTensor(),                   # Convertir a Tensor de PyTorch en rango [0, 1]
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]) # Normalización estándar de ImageNet
])

transformaciones_test = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# ---------------------------------------------------------------------
# PASO 5: Carga Automática de Datos (ImageFolder)
# ---------------------------------------------------------------------
# ImageFolder mapea automáticamente el nombre de las subcarpetas como las etiquetas.
# Ejemplo: si ve "perros" y "gatos", a perros le asignará 0 y a gatos 1 de forma alfabética.
train_dataset = ImageFolder(root=RUTA_TRAIN, transform=transformaciones_train)
test_dataset = ImageFolder(root=RUTA_TEST, transform=transformaciones_test)

# DataLoaders: Agrupan los datos en lotes (batches)
BATCH_SIZE = 32 # Puedes bajarlo a 16 si te da error de memoria (Out of Memory)
train_loader = DataLoader(dataset=train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# Imprimir las clases detectadas para verificar que todo esté en orden
clases = train_dataset.classes
print(f"Clases detectadas en Drive de forma alfabética: {clases}")
print(f"Mapeo de etiquetas: {train_dataset.class_to_idx}")
print(f"Total de imágenes de entrenamiento: {len(train_dataset)}")
print(f"Total de imágenes de prueba: {len(test_dataset)}\n")

# ---------------------------------------------------------------------
# PASO 6: Arquitectura de la Red Convolucional (Modificable)
# ---------------------------------------------------------------------
class MiCNNClasificador(nn.Module):
    def __init__(self):
        super(MiCNNClasificador, self).__init__()

        # Bloque de extracción de características (Convoluciones)
        self.features = nn.Sequential(
            # Capa 1: Entrada RGB (3 canales), 16 filtros de salida, kernel 3x3
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2), # Reduce tamaño a la mitad (112x112)

            # Capa 2: Recibe 16 canales, genera 32 filtros
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)  # Reduce tamaño a la mitad (56x56)
        )

        # Bloque de Clasificación (Capas Densas / Lineales)
        # 32 canales * 56 de alto * 56 de ancho = 100,352 neuronas de entrada al aplanar
        self.classifier = nn.Sequential(
            nn.Linear(32 * 56 * 56, 128),
            nn.ReLU(),
            nn.Dropout(0.5), # Evita el sobreajuste (overfitting) apagando el 50% de neuronas al azar
            nn.Linear(128, 2) # SALIDA = 2 porque es clasificación biclase (Clase A vs Clase B)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1) # Aplanar el mapa de características 2D a 1D
        x = self.classifier(x)
        return x

# Instanciar el modelo y enviarlo a la GPU/CPU
model = MiCNNClasificador().to(device)

# ---------------------------------------------------------------------
# PASO 7: Función de Pérdida y Optimidad
# ---------------------------------------------------------------------
criterion = nn.CrossEntropyLoss() # Ideal para clasificación
optimizer = optim.Adam(model.parameters(), lr=0.001) # Ritmo de aprendizaje (Learning Rate)

# ---------------------------------------------------------------------
# PASO 8: Bucle de Entrenamiento (Training Loop)
# ---------------------------------------------------------------------
NUM_EPOCHS = 5 # Modifica el número de épocas según requieras más entrenamiento
print("Iniciando el entrenamiento de la red...")

for epoch in range(NUM_EPOCHS):
    model.train()
    loss_acumulada = 0.0

    for imagenes, etiquetas in train_loader:
        # Mover datos al hardware seleccionado
        imagenes, etiquetas = imagenes.to(device), etiquetas.to(device)

        # Forward pass
        predicciones = model(imagenes)
        loss = criterion(predicciones, etiquetas)

        # Backward pass y optimización
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        loss_acumulada += loss.item()

    print(f"Época [{epoch+1}/{NUM_EPOCHS}] - Pérdida Promedio: {loss_acumulada/len(train_loader):.4f}")

print("¡Entrenamiento concluido!\n")

# ---------------------------------------------------------------------
# PASO 9: Evaluación Final en el Set de Prueba (Test)
# ---------------------------------------------------------------------
model.eval()
correctos = 0
total_imagenes = 0

# Desactivamos el cálculo de gradientes para ir más rápido y ahorrar memoria
with torch.no_grad():
    for imagenes, etiquetas in test_loader:
        imagenes, etiquetas = imagenes.to(device), etiquetas.to(device)
        outputs = model(imagenes)
        _, predicciones_indices = torch.max(outputs.data, 1)

        total_imagenes += etiquetas.size(0)
        correctos += (predicciones_indices == etiquetas).sum().item()

accuracy = 100 * correctos / total_imagenes
print(f"Exactitud (Accuracy) en el conjunto de TEST: {accuracy:.2f}%")