<?php
//Importar la base de datos de estudiantes de la UIS
require 'vendor/autoload.php';
use PhpOffice\PhpSpreadsheet\IOFactory;

$reader = IOFactory::createReader('Xlsx');
$spreadsheet = $reader->load('BD_EstudiantesUIS.xlsx');
$worksheet = $spreadsheet->getActiveSheet();

//Imprima el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
// Pida el numero de la carrera a listar, de la base de datos, lea los estudiantes de la carrera ingresada que tengan promedio acumulado igual o mayor a 4
// LA CARRERA SELECCIONADA corresponde a las dos primeras cifras de la columna A de la base de datos (codigo)

// 1. Imprimir el código y el nombre de los estudiantes de la carrera X que tengan promedio acumulado igual o mayor a 4
$carrera = readline("Ingrese el código de la carrera a listar: ");

$highestRow = $worksheet->getHighestRow();
$highestColumn = $worksheet->getHighestColumn();
$highestColumnIndex = \PhpOffice\PhpSpreadsheet\Cell\Coordinate::columnIndexFromString($highestColumn);

$estudiantes_carrera = array();
for ($row = 2; $row <= $highestRow; ++$row) {
    $codigo = $worksheet->getCellByColumnAndRow(1, $row)->getValue();
    if (substr($codigo, 0, 2) == $carrera) {
        $nombre = $worksheet->getCellByColumnAndRow(2, $row)->getValue();
        $promedio = $worksheet->getCellByColumnAndRow(3, $row)->getValue();
        if ($promedio >= 4) {
            $estudiantes_carrera[] = array('codigo' => $codigo, 'nombre' => $nombre, 'promedio' => $promedio);
        }
    }
}

echo "Estudiantes de la carrera " . $carrera . " con promedio acumulado igual o mayor a 4:\n";
foreach ($estudiantes_carrera as $estudiante) {
    echo $estudiante['codigo'] . " " . $estudiante['nombre'] . " " . $estudiante['promedio'] . "\n";
}
$num_estudiantes = count($estudiantes_carrera);
echo "Total de estudiantes con promedio igual o mayor a 4: " . $num_estudiantes . "\n";

//2. Imprimir el código y el nombre de los estudiantes que ingresaron antes de 1990 (la tercera cifra es 1 y la cuarta cifra menor que 9) y están condicionales (promedio entre 2.7 y 3.2).
$nineties = array();
for ($row = 2; $row <= $highestRow; ++$row) {
    $codigo = $worksheet->getCellByColumnAndRow(1, $row)->getValue();
    if (substr($codigo, 2, 1) == '1' && substr($codigo, 3, 1) < '9') {
        $nombre = $worksheet->getCellByColumnAndRow(2, $row)->getValue();
        $promedio = $worksheet->getCellByColumnAndRow(3, $row)->getValue();
        if ($promedio >= 2.7 && $promedio <= 3.2) {
            $nineties[] = array('codigo' => $codigo, 'nombre' => $nombre, 'promedio' => $promedio);
        }
    }
}

echo "Estudiantes que ingresaron antes de 1990 y están condicionales:\n";
foreach ($nineties as $estudiante) {
    echo $estudiante['codigo'] . " " . $estudiante['nombre'] . " " . $estudiante['promedio'] . "\n";
}
$num_nineties = count($nineties);
echo "Total de estudiantes que ingresaron antes de 1990 y están condicionales: " . $num_nineties . "\n";

?>