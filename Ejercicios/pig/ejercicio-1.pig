
/* Cargar datos */
ventas = LOAD '/user/ejercicios-pig/ventas.csv' USING PigStorage(',')
AS (id:int, fecha:chararray, producto:chararray, cantidad:int, precio:double);

/* Total de ventas por producto */
ventas_por_producto = GROUP ventas BY producto;
total_ventas = FOREACH ventas_por_producto GENERATE
    group AS producto,
    SUM(ventas.cantidad) AS total_cantidad;
DUMP total_ventas;

/* Ingreso por producto */
ingreso = FOREACH ventas GENERATE producto, (cantidad * precio) AS ingreso_producto;

ingreso_por_producto = GROUP ingreso BY producto;

total_ingreso = FOREACH ingreso_por_producto GENERATE
    group AS producto,
    SUM(ingreso.ingreso_producto) AS total_ingreso;

DUMP total_ingreso;

/* Productos con más de 2 ventas */
productos_populares = FILTER total_ventas BY total_cantidad > 2;

DUMP productos_populares;