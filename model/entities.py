from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import connector

Base = connector.Manager.Base


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    # One to many relationship with Compra
    compras = relationship('Compra', back_populates='usuario', lazy=True)

    
class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)

    # One to many relationship with Subcategoria
    subcategorias = relationship('Subcategoria', back_populates='categoria', lazy=True)


# Many to Many between Subcategoria - Producto
subcategoria_producto = Table(
    'subcategoria_producto', Base.metadata,
    Column('subcategoria_id', Integer, ForeignKey('subcategoria.id')),
    Column('producto_id', Integer, ForeignKey('producto.id'))
)


class Subcategoria(Base):
    __tablename__ = 'subcategoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    
    # Many to one relationship with Categoria
    categoria = relationship('Categoria', back_populates='subcategorias')

    # For Many to Many relationship with Producto
    productos = relationship('Producto', secondary=subcategoria_producto, back_populates='subcategorias')


# Many to Many between Compra - Producto
compra_producto = Table(
    'compra_producto', Base.metadata,
    Column('compra_id', Integer, ForeignKey('compra.id')),
    Column('producto_id', Integer, ForeignKey('producto.id'))
)


class Producto(Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    descripcion = Column(String(255))
    stock = Column(Integer)

    # For Many to Many relationship with Subcategoria
    subcategorias = relationship('Subcategoria', secondary=subcategoria_producto, back_populates="productos")

    # For Many to Many relationship with Compra
    compras = relationship('Compra', secondary=compra_producto, back_populates="productos")



class Compra(Base):
    __tablename__ = 'compra'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    fecha = Column(DateTime, nullable=False)

    # Many to one relationship with Usuario
    usuario = relationship('Usuario', back_populates = "compras")

    # For Many to Many relationship with producto
    productos = relationship('Producto', secondary=compra_producto, back_populates="compras")



if __name__ == '__main__':
    db = connector.Manager()
    engine = db.createEngine()