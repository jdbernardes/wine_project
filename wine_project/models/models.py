from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship


table_registry = registry()


@table_registry.mapped_as_dataclass
class Wine:
    __tablename__ = "wines"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    fixed_accidity: Mapped[float]
    volatile_acidity: Mapped[float]
    citric_acid: Mapped[float]
    residual_sugar: Mapped[float]
    chlorides: Mapped[float]
    free_sulfur_dioxide: Mapped[float]
    total_sulfur_dioxide: Mapped[float]
    density: Mapped[float]
    pH: Mapped[float]
    sulphates: Mapped[float]
    alcohol: Mapped[float]

    evaluated_wines: Mapped["EvaluatedWines"] = relationship(
        back_populates="wine", uselist=False, init=False, default=None
    )


@table_registry.mapped_as_dataclass
class EvaluatedWines:
    __tablename__ = "evaluated_wines"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    wine_id: Mapped[int] = mapped_column(ForeignKey("wines.id"), init=False)
    wine: Mapped[Wine] = relationship(back_populates="evaluated_wines")
    quality: Mapped[int]
