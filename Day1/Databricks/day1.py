# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Advent of Code 2021 - Day 1🎄

# COMMAND ----------

from pyspark.sql.types import *

# Set the schema up front.
schema = StructType([
    StructField("depthReading", IntegerType())
])

# import the file to a dataframe
df = (spark.read.csv("/FileStore/tables/day1_input_cporteou.txt",schema=schema))
df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Challenge 1

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql import functions as F
from pyspark.sql.functions import col

windowSpec  = Window.partitionBy().orderBy("rowId")

#Add a row id, bring in the previous value and calculate the diff
resultsdf = (df.withColumn("rowId", F.monotonically_increasing_id())
             .withColumn("previousReading", F.lag("depthReading").over(windowSpec).cast(IntegerType()))
             .withColumn("change",col("depthReading") - col("previousReading")))

resultsdf.show()


# COMMAND ----------

# Return a count of records where the change is greater than zero
resultsdf.where(resultsdf.change >= 0).count()

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ## Challenge 2
