from pyspark.sql import SparkSession

# Connect to the Spark Connect server
spark = SparkSession.builder \
    .appName("MongoDB Spark Connect") \
    .remote("sc://172.34.0.35:7077") \
    .config("spark.mongodb.read.connection.uri", "mongodb://bahati2:bahati2@172.34.0.22:27017/farmers.mycollection") \
    .config("spark.mongodb.read.database", "farmers") \
    .config("spark.mongodb.read.collection", "mycollection") \
    .getOrCreate()

# Read data from MongoDB
df = spark.read.format("mongodb").load()

# Show the schema of the DataFrame
df.printSchema()

# Perform some basic DataFrame operations
df_filtered = df.filter(df['Quantity (kg)'] > 50)
df_grouped = df_filtered.groupBy("County").count()

# Show the results of the operations
df_grouped.show()

# Stop the Spark session
spark.stop()
