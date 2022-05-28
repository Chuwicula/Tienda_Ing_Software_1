import sqlite3

#conexion BD
conn = sqlite3.connect('tiendita')

#creacion del cursos
cursor = conn.cursor()

#crear tablas
cursor.execute("""
    CREATE TABLE tipo_usuario(
        id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        rol VARCHAR(255)
    );
""")

cursor.execute("""CREATE TABLE estado(
        id_estado INT AUTO_INCREMENT PRIMARY KEY,
        nombre  VARCHAR(255)
);""")

cursor.execute("""CREATE TABLE tipo_pago(
        id_tipo_pago INT AUTO_INCREMENT PRIMARY KEY,
        nombre  VARCHAR(255)
    );
""")
cursor.execute("""
     CREATE TABLE cliente(
        id_cliente INT PRIMARY KEY,
        direccion VARCHAR(255),
        nombre VARCHAR(255)
    );
""")
cursor.execute("""
    CREATE TABLE articulo(
        id_articulo INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        valor INT,
        descuento INT
    );
""")
cursor.execute("""
CREATE TABLE usuario(
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        esta_activo BOOLEAN,
        fecha_creacion DATE,
        contrasenia_encryt VARCHAR(255),
        id_tipo_usuario INT,
        FOREIGN KEY(id_tipo_usuario) REFERENCES tipo_usuario(id_tipo_usuario)
    );
""")
cursor.execute("""
    CREATE TABLE pedido(
        id_pedido INT AUTO_INCREMENT PRIMARY KEY,
        id_usuario INT,
        id_cliente INT,
        id_estado INT,
        fecha DATE,
        id_tipo_pago INT,
        FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
        FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
        FOREIGN KEY(id_estado) REFERENCES estado(id_estado),
        FOREIGN KEY(id_tipo_pago) REFERENCES tipo_pago(id_tipo_pago)
    );
""")
cursor.execute("""
     CREATE TABLE articulos_pedido(
        id_articulos_pedido INT AUTO_INCREMENT PRIMARY KEY,
        id_pedido INT,
        id_articulo INT,
        FOREIGN KEY(id_pedido) REFERENCES pedido(id_pedido),
        FOREIGN KEY(id_articulo) REFERENCES articulo(id_articulo)
        )
""")

conn.commit()

conn.close()
