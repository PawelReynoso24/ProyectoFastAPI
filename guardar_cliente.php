<?php
// Conexión a la base de datos
$servername = "localhost";
$username = "root";
$password = "";
$database = "clientes";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

// Recoger datos del formulario
$nombre = $_POST['nombre'];
$apellido = $_POST['apellido'];
$correo = $_POST['correo'];

// Insertar datos en la tabla
$sql = "INSERT INTO clientes (nombre, apellido, correo) VALUES ('$nombre', '$apellido', '$correo')";

if ($conn->query($sql) === TRUE) {
    echo "Cliente registrado con éxito";
} else {
    echo "Error al registrar al cliente: " . $conn->error;
}

// Cerrar la conexión
$conn->close();
?>