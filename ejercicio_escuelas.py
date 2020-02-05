#Ojalá y cumpla con los requerimientos mínimos. Saludos colega.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine=create_engine('sqlite:///:memory:')
Base=declarative_base(engine)

class Student(Base):
    __tablename__="alumno"
    id=Column(Integer,Sequence('alumno_seq_id'),primary_key=True)
    nombrea=Column(String)
    curso_ida=Column(Integer,ForeignKey('curso.id'))
    courses=relationship("Course",back_populates='estudiantes')
    def __repr__(self):
        return'{}'.format(self.nombrea)

class Course(Base):
    __tablename__='curso'
    id=Column(Integer, Sequence('curso_seq_id'),primary_key=True)
    nombrec=Column(String)
    horario=Column(String)
    estudiantes=relationship("Student",back_populates='courses')
    
    maestros=relationship("Maestro",back_populates='cursillo')
    def __repr__(self):
        return'{}{}'.format(self.nombrec,self.horario)

class Maestro(Base):
    __tablename__='profesor'
    id=Column(Integer, Sequence('profesor_seq_id'),primary_key=True)
    nombrep=Column(String)
    curso_idp=Column(Integer,ForeignKey('curso.id'))
    
    cursillo=relationship("Course",back_populates='maestros')

    def __repr__(self):
        return'{}'.format(self.nombrep)

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

alumno1=Student(nombrea='Panchito')
print(alumno1)
session.add(alumno1)
alumno1.courses=Course(nombrec='Quimica',horario='7-8 pm')
print(alumno1.courses)

profesor1=Maestro(nombrep='Huidobro')
session.add(profesor1)
profesor1.cursillo=Course(nombrec='Quimica ',horario=' 7-8 pm')
print(profesor1.cursillo)
print(session.query(Course).filter(Maestro.cursillo.has()).all())

session.commit()
