"""Minimal script to test Databricks workspace connection via PySpark.
Works with both classic and serverless clusters (use a Databricks Connect version that supports serverless if needed).
"""
import os
from pathlib import Path

from databricks.connect import DatabricksSession

# Load .databricks/.databricks.env (cluster ID, etc.)
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

# Trivial PySpark call to verify connection
result = spark.sql("SELECT 1 AS one").collect()
print("Connection OK:", result[0]["one"] == 1)
