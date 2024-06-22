import pandas as pd
from pyadomd import Pyadomd

DatasetName = "MADI ALLE REPORTING"
PowerBIEndpoint = f"powerbi://api.powerbi.com/v1.0/myorg/MADI%20-%20Alle%20Datasets;"
connectionString = f"Provider=MSOLAP.8;Data Source={PowerBIEndpoint};User ID=;Password=;Initial Catalog={DatasetName}"

con  =  Pyadomd(connectionString)

con.open()
rs = con.cursor().execute("")
df = pd.DataFrame(rs.fetchone(), columns=["PARTITION_NAME"])
print(df)
con.close()