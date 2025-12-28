import csv
import pandas as pd
from sqlalchemy import select, delete
from .connection import SessionLocal, engine
from .model import CropObservation
from .generation import ensure_db_ready


# Load data
def load_csv(
    csv_path: str,
    chunk_size: int = 5000,
):
    ensure_db_ready(schema="iot")

    with SessionLocal.begin() as session:
        session.execute(delete(CropObservation))

        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            batch = []

            for row in reader:
                batch.append(
                    {
                        "canopy_coverage": float(row["Canopy_Coverage"]),
                        "chlorophyll_content": float(row["Chlorophyll_Content"]),
                        "leaf_area_index": float(row["Leaf_Area_Index"]),
                        "temperature": float(row["Temperature"]),
                        "humidity": float(row["Humidity"]),
                        "rainfall": float(row["Rainfall"]),
                        "wind_speed": float(row["Wind_Speed"]),
                        "soil_moisture": float(row["Soil_Moisture"]),
                        "soil_ph": float(row["Soil_pH"]),
                        "organic_matter": float(row["Organic_Matter"]),
                        "weed_coverage": float(row["Weed_Coverage"]),
                        "pest_damage": int(row["Pest_Damage"]),
                        "pest_hotspots": int(row["Pest_Hotspots"]),
                        "crop_growth_stage": int(row["Crop_Growth_Stage"]),
                        "crop_type": row["Crop_Type"],
                        "crop_stress_indicator": int(row["Crop_Stress_Indicator"]),
                    }
                )

                if len(batch) >= chunk_size:
                    session.execute(
                        CropObservation.__table__.insert(),
                        batch,
                    )
                    batch.clear()

            if batch:
                session.execute(
                    CropObservation.__table__.insert(),
                    batch,
                )


def fetch_all():
    with engine.begin() as connection:
        stmt = select(CropObservation)
        return pd.read_sql(stmt, connection)


if __name__ == "__main__":
    load_csv("data.csv")
