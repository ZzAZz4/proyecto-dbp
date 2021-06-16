from flask_sqlalchemy import SQLAlchemy
from database.connector import Manager
from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = Manager.Base

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    subcategorias = relationship('Subcategoria', backref='categoria', lazy=True)

class Subcategoria(Base):
    __tablename__ = 'subcategoria'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    producto_id = Column(Integer, ForeignKey('producto.id'))
    productos = relationship('Producto', back_populates="subcategoria")

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    precio = Column(Double, nullable=False)
    descripcion = Column(String(255))
    stock = Column(Integer)
    subcategorias = relationship('Subcategoria', back_populates="productos")

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    compras = relationship('Compra', backref='usuarios', lazy=True)

class Compra(Base):
    __tablename__ = 'compra'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    fecha = Column(D)
    productos = relationship('productos', secondary=compra_producto)

compra_producto = Table(
    'compra_producto', Base.metadata,
    Column('compra_id', Integer, ForeignKey('compra.id')),
    Column('producto_id', Integer, ForeignKey('productos.id'))
)

if __name__ == '__main__':
    