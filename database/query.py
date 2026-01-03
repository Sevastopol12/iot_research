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
                        "timestamp": pd.to_datetime(row["Timestamp"]).to_pydatetime(),
                        "plant_id": int(row["Plant_ID"]),
                        "soil_moisture": float(row["Soil_Moisture"]),
                        "ambient_temperature": float(row["Ambient_Temperature"]),
                        "soil_temperature": float(row["Soil_Temperature"]),
                        "humidity": float(row["Humidity"]),
                        "light_intensity": float(row["Light_Intensity"]),
                        "soil_ph": float(row["Soil_pH"]),
                        "nitrogen_level": float(row["Nitrogen_Level"]),
                        "phosphorus_level": float(row["Phosphorus_Level"]),
                        "potassium_level": float(row["Potassium_Level"]),
                        "chlorophyll_content": float(row["Chlorophyll_Content"]),
                        "electrochemical_signal": float(row["Electrochemical_Signal"]),
                        "plant_health_status": row["Plant_Health_Status"],
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
