import os
from pathlib import Path

from databricks.connect import DatabricksSession

# Load .databricks/.databricks.env so cluster ID (and other vars) are set when using Run button
_env_file = Path(__file__).resolve().parent / ".databricks" / ".databricks.env"
if _env_file.exists():
    with open(_env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

builder = DatabricksSession.builder
if os.environ.get("DATABRICKS_CLUSTER_ID"):
    builder = builder.clusterId(os.environ["DATABRICKS_CLUSTER_ID"])
spark = builder.getOrCreate()

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)