Sistema para escuelas en sqlalchemy como parte del curso de "Bases de datos en Python"

Consigna:
Se invita a crear un sistema para una escuela mediante SQLAlchemy. Este sistema permite registrar nuevos alumnos, profesores y cursos.

Un alumno es asignado a un curso y un curso puede tener asociado más de un profesor. Los profesores tienen un horario que indica cuando están en cada curso.

El horario asociará un curso y un profesor para un día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo), una hora desde y una hora hasta.

El sistema permitirá exportar los alumnos que pertenecen a un curso, el horario de cada profesor y el horario del curso.

Se agradece los comentarios o sugerencias que puedan otorgar.

Nota:
Se consideró que la entidad "horario" poseerá dos claves foráneas que harán referencia tanto a "Curso" como "Profesor" . Se anexa diagrama Entidad-Relación. Otra entidad a poseer una entidad con clave foránea es "alumno"
