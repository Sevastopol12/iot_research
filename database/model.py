from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, Float, String, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class CropObservation(Base):
    __tablename__ = "crop"
    __table_args__ = {"schema": "iot"}

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # Time series
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, name="timestamp"
    )
    plant_id: Mapped[int] = mapped_column(Integer, nullable=False, name="plant_id")

    # env_features
    soil_moisture: Mapped[float] = mapped_column(
        Float, nullable=False, name="soil_moisture"
    )
    ambient_temperature: Mapped[float] = mapped_column(
        Float, nullable=False, name="ambient_temperature"
    )
    soil_temperature: Mapped[float] = mapped_column(
        Float, nullable=False, name="soil_temperature"
    )
    humidity: Mapped[float] = mapped_column(Float, nullable=False, name="humidity")
    light_intensity: Mapped[float] = mapped_column(
        Float, nullable=False, name="light_intensity"
    )

    # soil_features
    soil_ph: Mapped[float] = mapped_column(Float, nullable=False, name="soil_ph")
    nitrogen_level: Mapped[float] = mapped_column(
        Float, nullable=False, name="nitrogen_level"
    )
    phosphorus_level: Mapped[float] = mapped_column(
        Float, nullable=False, name="phosphorus_level"
    )
    potassium_level: Mapped[float] = mapped_column(
        Float, nullable=False, name="potassium_level"
    )

    # phys_features
    chlorophyll_content: Mapped[float] = mapped_column(
        Float, nullable=False, name="chlorophyll_content"
    )
    electrochemical_signal: Mapped[float] = mapped_column(
        Float, nullable=False, name="electrochemical_signal"
    )
    # Label
    plant_health_status: Mapped[str] = mapped_column(
        String(50), nullable=False, name="plant_health_status"
    )
