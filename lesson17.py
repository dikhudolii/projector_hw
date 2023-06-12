import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://localhost:5432/postgres')

Base = sqlalchemy.orm.declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    subjects = relationship('Subject', secondary='student_subject', back_populates='students')


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship('Student', secondary='student_subject', back_populates='subjects')


student_subject_table = Table('student_subject', Base.metadata,
                              Column('student_id', Integer, ForeignKey('students.id')),
                              Column('subject_id', Integer, ForeignKey('subjects.id'))
                              )

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

english_class = session.query(Subject).filter(Subject.name == 'English').first()

if english_class:
    students = english_class.students
    for student in students:
        print(student.name)
