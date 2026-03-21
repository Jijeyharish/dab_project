import os
import sys
import pytest
sys.path.append(os.getcwd())



@pytest.fixture()
def spark():
    try:
        from databricks.connect import DatabricksSession
        spark=DatabricksSession.builder.serverless(True).getOrCreate()
        print('using Databricks session')
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark=SparkSession.builder.getOrCreate()
            print('using Spark Session')
        except ImportError:
            raise ImportError('neither spark nor Databricks session')
    return spark