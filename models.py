from sqlalchemy import Column, Integer, String
from databse import Base

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(125), unique=False)
    autor = Column(String(125), unique=False)

    def __init__(self, titulo=None, autor=None):
        self.titulo = titulo
        self.autor = autor
    
    def as_dict(self):
        return {"id": self.id, "titulo": self.titulo, "autor": self.autor}

    def __repr__(self):
        return f'<Titulo {self.titulo}>'