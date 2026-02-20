import os
from databricks.connect import DatabricksSession

# Uses ~/.databrickscfg [DEFAULT] for host/token. Cluster ID must be set, e.g.:
#   source .databricks/.databricks.env   # (from project root, sets DATABRICKS_CLUSTER_ID)
builder = DatabricksSession.builder
if os.environ.get("DATABRICKS_CLUSTER_ID"):
    builder = builder.clusterId(os.environ["DATABRICKS_CLUSTER_ID"])
spark = builder.getOrCreate()

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)