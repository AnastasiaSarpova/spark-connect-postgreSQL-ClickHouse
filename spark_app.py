
from pyspark.sql import SparkSession
import os

# Объединяем оба JAR-файла для ClickHouse и PostgreSQL в один список
jar_files = [
    "clickhouse-jdbc-0.6.3-all.jar", 
    "postgresql-42.7.4.jar"]


# Создаём один SparkSession для обоих соединений
spark = (SparkSession.builder
         .appName("spark_jdbc_connections")
         .master("local")
         .config("spark.jars", ",".join(jar_files))
         .getOrCreate())

# Загружаем из ClickHouse
url_click = "jdbc:ch://localhost:8123/default"
user_ch = os.environ.get("CLICKHOUSE_USER")
password_ch = os.environ.get("CLICKHOUSE_PASSWORD")
query_ch = "SELECT * FROM demo_table"
driver_ch = "com.clickhouse.jdbc.ClickHouseDriver"

df_clickhouse = (spark.read
      .format('jdbc')
      .option('driver', driver_ch)
      .option('url', url_click)
      .option('user', user_ch)
      .option('password', password_ch)
      .option('query', query_ch)
      .load())
print("Данные из ClickHouse:")
df_clickhouse.show()

# Загружаем из Postgres
url_pg = "jdbc:postgresql://localhost:5432/postgres"
user_pg = os.environ.get("POSTGRES_USER")
password_pg = os.environ.get("POSTGRES_PASSWORD")
query_pg = "SELECT * FROM demo_table"
driver_pg = "org.postgresql.Driver"

df_postgres = (spark.read
      .format('jdbc')
      .option('driver', driver_pg)
      .option('url', url_pg)
      .option('user', user_pg)
      .option('password', password_pg)
      .option('query', query_pg)
      .load())
print("Данные из PostgreSQL:")
df_postgres.show()


spark.stop()