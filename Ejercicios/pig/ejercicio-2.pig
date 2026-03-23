/* 1. Cargar datos */
pedidos = LOAD '/user/ejercicios-pig/pedidos.csv' USING PigStorage(',')
AS (id:int, fecha:chararray, plato:chararray, cantidad:int, precio:double);

/* 2. Total de platos vendidos por tipo */
pedidos_por_plato = GROUP pedidos BY plato;

total_platos = FOREACH pedidos_por_plato GENERATE group AS plato, SUM(pedidos.cantidad) AS total_cantidad;

DUMP total_platos;

/* 3. Ingreso total por plato */
ingresos = FOREACH pedidos GENERATE plato, (cantidad * precio) AS ingreso_plato;

ingresos_por_plato = GROUP ingresos BY plato;

total_ingresos = FOREACH ingresos_por_plato GENERATE group AS plato, SUM(ingresos.ingreso_plato) AS total_ingreso;

DUMP total_ingresos;

/* 4. Platos con más de 3 unidades vendidas */
platos_populares = FILTER total_platos BY total_cantidad > 3;

DUMP platos_populares;