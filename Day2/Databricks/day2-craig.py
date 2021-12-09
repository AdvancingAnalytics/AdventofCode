# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Advent of Code 2021 - Day 2🎄

# COMMAND ----------

# Load puzzle input

from pyspark.sql.types import *

# Set the schema up front.
schema = StructType([
    StructField("direction", StringType()),
    StructField("value", IntegerType())
])

# import the file to a dataframe
df = (spark.read
         .option("delimiter", " ")
         .csv("/FileStore/tables/day2_input_cporteou.txt",schema=schema))
df.show()

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ## Challenge 1

# COMMAND ----------

# Turn up values into negatives
from pyspark.sql import functions as F

resultsDf = (df.withColumn("updatedValue", F.when(df.direction == "up", -df.value)
      .otherwise(df.value)))
    
resultsDf.show()

# COMMAND ----------


resultsDf.where(resultsDf.direction == "forward").agg({'updatedValue': 'sum'}).show()

resultsDf.where((resultsDf.direction == "down") | (resultsDf.direction == "up")).agg({'updatedValue': 'sum'}).show()

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Challenge 2

# COMMAND ----------

resultsDf.show()


# COMMAND ----------



# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

windowSpec  = Window.partitionBy().orderBy("rowId")

aimDf = (resultsDf.withColumn("rowId", F.monotonically_increasing_id())
#          .withColumn("aim", when((resultsDf.direction == "down") | (resultsDf.direction == "up") , F.sum(resultsDf.updatedValue).over(windowSpec)).otherwise(0))).show()
        .withColumn("aim", when((resultsDf.direction == "down") | (resultsDf.direction == "up"), resultsDf.updatedValue).otherwise(0))
        .withColumn("horizontalPosition", when(resultsDf.direction == "forward", resultsDf.updatedValue).otherwise(0))
        .withColumn("depth",when(resultsDf.direction == "forward", (resultsDf.updatedValue * F.sum("aim").over(windowSpec))).otherwise(0)))
           
#          .withColumn("aim", F.sum(resultsDf.updatedValue).over(windowSpec))).show()
  

#      sum('value').over(Window.orderBy('order_col'))

# COMMAND ----------

aimDf.show()


# COMMAND ----------

aimDf.agg({'horizontalPosition': 'sum'}).show()

aimDf.agg({'depth': 'sum'}).show()

aimDf.select((F.sum(aimDf.horizontalPosition) * F.sum(aimDf.depth)).alias("result")).show()
