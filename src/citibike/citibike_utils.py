from pyspark.sql.functions import *
def get_trip_duration_mins(spark,df,start_col,end_col,output_col):
    return df.withColumn(output_col,
                         ((col(end_col).cast("long") - col(start_col).cast("long")) / 60)
    )