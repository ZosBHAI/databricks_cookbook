# Azure Databricks Workspace deployment

### Notes

1. Control plane , by default, uses public ip
to access Data plane. 
2. 2 types of deployment - Default deployment & VNet ingestion.

2. VNet injection is the recommended for production deployment.
3. In VNET injestion, you can use the existing virtual network and will more control over the network rules.
4. Even in VNET injestion, by default control plane and data plane communicate using public ip.
5. In VNET injestion, Databricks need virtual network where the size of public and private should be same.
6. Following things to be considered while determining  the CIDR range
        - Number of concurrent nodes running in cluster.
        - 2 X (1 for public and another for private subnet)
        - 4 X number of concurrent nodes.
        - Under each subnets, 5 addresses are reserved.
