# Databricks notebook source
directory_id = dbutils.secrets.get(scope="mountadlsapp",key="tenantid")
app_id = dbutils.secrets.get(scope="mountadlsapp",key="mountappid")
client_secret = dbutils.secrets.get(scope="mountadlsapp",key="mountappsecretvalue")


# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": app_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://dbhive@dbrickexternaldev.dfs.core.windows.net/",
  mount_point = "/mnt/dbhive",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/dbhive/tables/")

# COMMAND ----------

dbutils.fs.refreshMounts()
