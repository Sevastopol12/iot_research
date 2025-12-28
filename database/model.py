from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Integer, Float, String


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
    

    # Sensors
    temperature: Mapped[float] = mapped_column(Float, nullable=False)
    humidity: Mapped[float] = mapped_column(Float, nullable=False)
    rainfall: Mapped[float] = mapped_column(Float, nullable=False)
    wind_speed: Mapped[float] = mapped_column(Float, nullable=False)

    # Handheld devices
    chlorophyll_content: Mapped[float] = mapped_column(Float, nullable=False)
    soil_moisture: Mapped[float] = mapped_column(Float, nullable=False)
    soil_ph: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Lab devices
    organic_matter: Mapped[float] = mapped_column(Float, nullable=False)

    # Output from image-devices    
    pest_damage: Mapped[int] = mapped_column(Integer, nullable=False)
    pest_hotspots: Mapped[int] = mapped_column(Integer, nullable=False)
    crop_growth_stage: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Satellite / bird-eye view images
    weed_coverage: Mapped[float] = mapped_column(Float, nullable=False)
    canopy_coverage: Mapped[float] = mapped_column(Float, nullable=False)
    leaf_area_index: Mapped[float] = mapped_column(Float, nullable=False)

    # Category
    crop_type: Mapped[str] = mapped_column(String(50), nullable=False)

    # Label
    crop_stress_indicator: Mapped[int] = mapped_column(Integer, nullable=False)

