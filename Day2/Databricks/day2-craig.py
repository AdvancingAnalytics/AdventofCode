# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Advent of Code 2021 - Day 1🎄

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
from pyspark.sql.functions import when

resultsDf = (df.withColumn("updatedValue", when(df.direction == "up", -df.value)
      .otherwise(df.value)))
    
resultsDf.show()

# COMMAND ----------


resultsDf.where(resultsDf.direction == "forward").agg({'updatedValue': 'sum'}).show()

#resultsDf.where((resultsDf.direction == "down") | (resultsDf.direction == "up")).show()
resultsDf.where((resultsDf.direction == "down") | (resultsDf.direction == "up")).agg({'updatedValue': 'sum'}).show()

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Challenge 2

# COMMAND ----------


