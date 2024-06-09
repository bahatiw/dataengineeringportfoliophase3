from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType

# Initialize Spark session with Kafka dependencies
spark = SparkSession.builder \
  .appName("KafkaSparkStreaming") \
  .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0,org.apache.kafka:kafka-clients:2.8.0") \
  .getOrCreate()

# Define Kafka parameters
kafka_brokers = "172.34.0.19:9092"
kafka_topic = "dataengineringportfolio"
group_id = 'dataengineering'

# Define schema for the JSON data
json_schema = StructType([
  StructField("County", StringType(), True),
  StructField("Farmer Name", StringType(), True),
  StructField("Produce", StringType(), True),
  StructField("Quantity (kg)", StringType(), True)
  # Add additional fields as necessary
])

# Read from Kafka
kafka_df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", kafka_brokers) \
  .option("subscribe", kafka_topic) \
  .option("startingOffsets", "earliest") \
  .option("kafka.group.id", group_id) \
  .load()

# Extract the value from the Kafka message and cast it to string
messages_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Parse the JSON data
parsed_df = messages_df.withColumn("value", from_json(col("value"), json_schema)).select("key", "value.*")

# Write the processed stream to the console (or any other sink)
query = parsed_df.writeStream \
  .outputMode("append") \
  .format("console") \
  .start()

query.awaitTermination()
