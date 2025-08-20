import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Создаём таблицу (один раз)
Base.metadata.create_all(engine)

@pytest.fixture
def session():
    s = Session()
    try:
        yield s
    finally:
        s.close()

def test_add_student(session):
    "Добавление студента"
    new_student = Student(name="Ivan Ivanov")
    session.add(new_student)
    session.commit()
    assert new_student.id is not None
    # Удаляем после теста
    session.delete(new_student)
    session.commit()

def test_update_student(session):
    "Изменение студента"
    s = Student(name="Petr Petrov")
    session.add(s)
    session.commit()
    s.name = "Petr Sidorov"
    session.commit()
    updated = session.query(Student).get(s.id)
    assert updated.name == "Petr Sidorov"
    session.delete(updated)
    session.commit()

def test_delete_student(session):
    "удаление студента"
    s = Student(name="Mark Smirnov")
    session.add(s)
    session.commit()
    student_id = s.id
    session.delete(s)
    session.commit()
    # Проверим, что студента нет
    assert session.query(Student).get(student_id) is None
