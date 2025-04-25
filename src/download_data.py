import os
# SETEA ESTA VARIABLE **ANTES** DE CUALQUIER IMPORT DE KAGGLE
os.environ['KAGGLE_CONFIG_DIR'] = os.path.join(os.path.dirname(__file__), '..', '.kaggle')

from kaggle.api.kaggle_api_extended import KaggleApi


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(DATA_DIR, exist_ok=True)
KAGGLE_DATASET = "mohamedbakhet/amazon-books-reviews"

def download_kaggle_dataset(dataset, dest_dir):
    print(f"Descargando dataset '{dataset}' a: {dest_dir}")
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=dest_dir, unzip=True, quiet=False)  # Muestra barra de progreso
    print("¡Descarga completa!")

if __name__ == "__main__":
    download_kaggle_dataset(KAGGLE_DATASET, DATA_DIR)
