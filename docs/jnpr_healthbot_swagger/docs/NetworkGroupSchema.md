# NetworkGroupSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description about the network group | [optional] 
**network_group_name** | **str** | Name of the network group. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**logging** | [**NetworkgroupSchemaLogging**](NetworkgroupSchemaLogging.md) |  | [optional] 
**reports** | **list[str]** |  | [optional] 
**notification** | [**DevicegroupSchemaNotification**](DevicegroupSchemaNotification.md) |  | [optional] 
**playbooks** | **list[str]** |  | [optional] 
**scheduler** | [**list[DevicegroupSchemaScheduler]**](DevicegroupSchemaScheduler.md) | List of schedulers associated with the playbook instances | [optional] 
**variable** | [**list[DevicegroupSchemaVariable]**](DevicegroupSchemaVariable.md) | Playbook variable configuration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

