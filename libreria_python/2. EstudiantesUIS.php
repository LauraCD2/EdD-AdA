<?php

//Importar la base de datos de estudiantes de la UIS
require 'vendor/autoload.php';
use PhpOffice\PhpSpreadsheet\IOFactory;
use PhpOffice\PhpSpreadsheet\Spreadsheet;

$spreadsheet = IOFactory::load("BD_EstudiantesUIS.xlsx");
$sheet = $spreadsheet->getActiveSheet();

//1. Imprimir el código y el nombre de los estudiantes de la carrera X (debe leerse el código de la carrera a listar) que tengan promedio acumulado igual o mayor a 4 y decir cuántos fueron.
//Pida el número de la carrera a listar, de la base de datos, lea los estudiantes de la carrera ingresada que tengan promedio acumulado igual o mayor a 4
//LA CARRERA SELECCIONADA corresponde a las dos primeras cifras de la columna A de la base de datos (codigo)
$carrera = readline("Ingrese el código de la carrera a listar: ");

$estudiantes_carrera = [];
$estudiantes_cuatro = [];

foreach ($sheet->getRowIterator() as $row) {
    $codigo = $sheet->getCell('A' . $row->getRowIndex())->getValue();
    $nombre = $sheet->getCell('B' . $row->getRowIndex())->getValue();
    $promedio = $sheet->getCell('C' . $row->getRowIndex())->getValue();

    if (substr($codigo, 0, 2) == $carrera) {
        array_push($estudiantes_carrera, array($codigo, $nombre, $promedio));

        if ($promedio >= 4) {
            array_push($estudiantes_cuatro, array($codigo, $nombre, $promedio));
        }
    }
}

//Imprimir código y nombre de los estudiantes de la carrera X con promedio acumulado igual o mayor a 4
echo "Estudiantes de la carrera " . $carrera . " con promedio acumulado igual o mayor a 4:\n";

foreach ($estudiantes_cuatro as $estudiante) {
    echo $estudiante[0] . " " . $estudiante[1] . " " . $estudiante[2] . "\n";
}

//Contar estudiantes con promedio mayor o igual a 4 de la carrera X
$num_estudiantes = count($estudiantes_cuatro);
echo "Total de estudiantes con promedio igual o mayor a 4: " . $num_estudiantes . "\n";

//2. Imprimir el código y el nombre de los estudiantes que ingresaron antes de 1990 (la tercera cifra es 1 y la cuarta cifra menor que 9) y están condicionales (promedio entre 2.7 y 3.2).
$novecond = [];

foreach ($sheet->getRowIterator() as $row) {
    $codigo = $sheet->getCell('A' . $row->getRowIndex())->getValue();
    $nombre = $sheet->getCell('B' . $row->getRowIndex())->getValue();
    $promedio = $sheet->getCell('C' . $row->getRowIndex())->getValue();

    if (substr($codigo, 2, 1) == '1' && substr($codigo, 3, 1) < '9' && $promedio >= 2.7 && $promedio <= 3.2) {
        array_push($novecond, array($codigo, $nombre, $promedio));
    }
}

//Imprimir código y nombre de los estudiantes que ingresaron antes de 1990 y están condicionales
echo "Estudiantes que ingresaron antes de 1990 y están condicionales:\n";
