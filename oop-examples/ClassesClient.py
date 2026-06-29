

from decimal import Decimal
from sqlalchemy import create_engine, String, Numeric, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# 1. Define the connection URL for your MySQL Database
# Format: mysql+pymysql://username:password@host:port/database_name
DATABASE_URL = "mysql+pymysql://practice:practice@localhost:3306/example_database"

# 2. Create the engine object
engine = create_engine(DATABASE_URL, echo=True)  # echo=True prints generated SQL logs


# 3. Create a Base class for Declarative Mapping
class Base(DeclarativeBase):
    pass

# 4. Define the Employee Model (Table Schema)
class Employee(Base):
    __tablename__ = "employees"

    # Mapped[] types specify Python data types, mapped_column specifies SQL options
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department: Mapped[str] = mapped_column(String(50), nullable=False)
    salary: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    def __repr__(self) -> str:
        return f"Employee(id={self.id}, name='{self.name}', department='{self.department}', salary={self.salary})"

# 5. Execute Database Operations
if __name__ == "__main__":
    # Create the table in MySQL if it doesn't already exist
    Base.metadata.create_all(engine)
    print("\n--- Table created successfully ---\n")
# Open a session to interact with the database
    with Session(engine) as session:
        # --- INSERT RECORDS ---
        emp1 = Employee(name="Alice Smith", department="Engineering", salary=Decimal("85000.00"))
        emp2 = Employee(name="Bob Jones", department="Marketing", salary=Decimal("62000.50"))
        session.add_all([emp1, emp2])
        session.commit()  # Save changes to the database