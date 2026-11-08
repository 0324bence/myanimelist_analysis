from pathlib import Path

from kagglehub import dataset_download


DATASET = "hernan4444/anime-recommendation-database-2020"
OUTPUT_DIR = Path(__file__).resolve().parent / "data"


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
dataset_download(DATASET, output_dir=str(OUTPUT_DIR))

print(f"Dataset downloaded to {OUTPUT_DIR}")
