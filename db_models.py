from sqlalchemy import String, CHAR, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Branch(Base):
    __tablename__ = "branches"

    code: Mapped[str] = mapped_column(String(3), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50), nullable=False)
    id_prefix: Mapped[str] = mapped_column(CHAR(2), unique=True, nullable=False)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[str] = mapped_column(CHAR(7), primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    branch: Mapped[str] = mapped_column(String(3),ForeignKey("branches.code"), nullable=False)
    cgpa: Mapped[float] = mapped_column(Numeric(4, 2), nullable=False)

