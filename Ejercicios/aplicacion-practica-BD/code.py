import re
from statistics import LinearRegression
import pyspark.sql.functions as F
from pyspark.ml.feature import VectorAssembler, VectorIndexer, OneHotEncoder, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

user = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
userName = re.sub(r"[^a-zA-Z0-9]", "_", user)

databaseName = userName + "_db"

spark.sql(f"CREATE DATABASE IF NOT EXISTS `{databaseName}`")
spark.sql("USE `{}`".format(databaseName))

print("Using database :::", databaseName)

dataPath = '/Volumes/workspace/crobledos01_educarex_es_db/volume/boston_housing_esp.csv'
display(dbutils.fs.ls(dataPath))

viviendasDF = (spark.read            # The DataFrameReader
   .option("header", "true")       # Use first line of all files as header
   .option("inferSchema", "true")  # Automatically infer data types
   .csv(dataPath)                  # Creates a DataFrame from CSV after reading in the file
)

display(viviendasDF)

viviendasDF.write.mode("overwrite").format("delta").saveAsTable("viviendas")

viviendasDF.printSchema()

display(viviendasDF.describe())

display(viviendasDF.groupBy('calefaccion').count())

display(viviendasDF.groupBy('calefaccion', 'consumo_calefacion').count())

display(viviendasDF.groupBy('calefaccion').count().orderBy('calefaccion'))

viviendasDF = viviendasDF.withColumn('universitarios', F.col('universitarios').cast('string')) \
                       .withColumn('chimenea', F.col('chimenea').cast('string'))
display(viviendasDF)

viviendaCleanDF = viviendasDF \
                 .select("antiguedad", "metros_habitables", "dormitorios", "chimenea", "calefaccion", "consumo_calefacion")

viviendaCleanDF.printSchema()

print(viviendaCleanDF.count())

viviendaCleanDF = viviendaCleanDF.na.drop()

calefaccion_indexer = StringIndexer(inputCol = 'calefaccion', outputCol = 'calefaccionIndexer')
calefaccion_encoder = OneHotEncoder(inputCol ='calefaccionIndexer', outputCol= 'calefaccionVec')
chimenea_indexer = StringIndexer(inputCol = 'chimenea', outputCol = 'chimeneaIndexer')
chimenea_encoder = OneHotEncoder(inputCol ='chimeneaIndexer', outputCol= 'chimeneaVec')

assembler = VectorAssembler(inputCols=[
    "antiguedad", "metros_habitables", "dormitorios",
    "chimeneaVec"
], outputCol='features')

lin_reg = LinearRegression(featuresCol='features', labelCol='consumo_calefacion')

pipeline = Pipeline(stages=[calefaccion_indexer,
                            calefaccion_encoder,
                            chimenea_indexer,
                            chimenea_encoder,
                            assembler,lin_reg])

train_data, test_data = viviendaCleanDF.randomSplit([0.7,0.3])

fit_model = pipeline.fit(train_data)

predictions = fit_model.transform(test_data)

predictions.printSchema()

display(predictions.select("Survived", "prediction"))
