from databricks.connect import DatabricksSession

# Choose one:
# A) Use profile-based serverless (DEFAULT profile has serverless_compute_id=auto)
# spark = DatabricksSession.builder.getOrCreate()

# B) Or explicit serverless in code
spark = DatabricksSession.builder.serverless().profile("DEFAULT").getOrCreate()

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
