##traduzca a php el anterior codigo de python:
<?php
//vector con los votos de cada candidato, cantidad max de votos = 5000
$votos = array();
for ($i = 0; $i < 30; $i++) {
    $votos[$i] = rand(1, 5000);
}

//suma de votos
$total_votos = array_sum($votos);

//normalizar los votos // formula matematica: votos_normalizados = votos / suma_votos * valor_objetivo

$votos_normalizados = array();
for ($i = 0; $i < 30; $i++) {
    $votos_normalizados[$i] = $votos[$i] / $total_votos * 5000;
}

//redondear los votos normalizados
for ($i = 0; $i < 30; $i++) {
    $votos_normalizados[$i] = round($votos_normalizados[$i]);
}

//vector con los candidatos
$candidatos = array();
for ($i = 0; $i < 30; $i++) {
    $candidatos[$i] = $i + 1;
}

//ordenar los votos de mayor a menor numero de votos
for ($i = 0; $i < 30; $i++) {
    for ($j = 0; $j < 30; $j++) {
        if ($votos_normalizados[$i] > $votos_normalizados[$j]) {
            $votos_normalizados[$i] = $votos_normalizados[$j];
            $candidatos[$i] = $candidatos[$j];
        }
    }
}

//imprimir de mayor a menor numero de votos
echo "El listado de mayor a menor, según el número de votos obtenidos por cada candidato es:";
for ($i = 0; $i < 30; $i++) {
    echo "El candidato ", $candidatos[$i], " obtuvo ", $votos_normalizados[$i], " votos";
}

//comprobar que la suma de votos es igual a 5000
//echo "La suma total de votos es: ", array_sum($votos_normalizados);
?>

