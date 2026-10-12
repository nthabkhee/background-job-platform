
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(
        String(20),
        default="pending",
    )
