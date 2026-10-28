from sqlalchemy import String, CHAR, Numeric, CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Branch(Base):
    __tablename__ = "branches"
    __table_args__ = (
        UniqueConstraint("id_prefix", name="unique_id_prefix"),
    )

    code: Mapped[str] = mapped_column(String(3), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable=False)
    id_prefix: Mapped[str] = mapped_column(CHAR(2), unique=True, nullable=False)


class Student(Base):
    __tablename__ = "students"
    __table_args__ = (
        CheckConstraint("cgpa >= 0.00 AND cgpa <= 10.0", name="students_cgpa_check"),
    )

    id: Mapped[str] = mapped_column(CHAR(7), primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    branch: Mapped[str] = mapped_column(String(3), ForeignKey("branches.code"), nullable=False)
    cgpa: Mapped[float] = mapped_column(Numeric(4, 2), nullable=False)

