# JobsFilterBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this background job object | [optional] 
**firm_id** | **int** | ID of the owning firm | [optional] 
**job_type** | **str** | The type of this job. Currently either b for a billing report, pdfrp for a PDF report, or bd for a bulk download | [optional] 
**created_dt_utc** | **datetime** | Create timestamp in UTC | [optional] 
**last_updated_dt_utc** | **datetime** | The last date and time this Background Job was updated | [optional] 
**queued_dt_utc** | **datetime** | The last date and time this Background Job was queued | [optional] 
**started_dt_utc** | **datetime** | The last date and time this Background Job was started | [optional] 
**finished_dt_utc** | **datetime** | The last date and time this Background Job was finished | [optional] 
**failed_dt_utc** | **datetime** | The last date and time this Background Job was failed | [optional] 
**created_by_id** | **int** | The user id for the user who created this Background Job | [optional] 
**is_finished** | **bool** | Returns true if the job is finished | [optional] 
**is_running** | **bool** | Returns true if the job has been dequeued and is running | [optional] 
**is_failed** | **bool** | Returns true if the job failed due to an exception | [optional] 
**is_revoked** | **bool** | Returns true if the job was cancelled by the user | [optional] 
**num_steps** | **int** | The progress of a job. Note that the number of steps might not be known until the job is dequeued. | [optional] 
**current_step** | **int** | Zero corresponds to the job waiting to be processed | [optional] 
**email_notification** | **datetime** | If true, this sends an email notification to the user who created the job | [optional] 
**email_notification_dt_utc** | **datetime** | The timestamp at which the email notification was sent. Only applies when email_notification is enabled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

