# Firm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this firm object | [optional] 
**parent_firm_id** | **int** | ID of the parent firm, if applicable | [optional] 
**permissions** | **list[str]** | List of permissions accessible to the firm. See Permissions Overview. | [optional] 
**name** | **str** | Firm name | [optional] 
**short_name** | **str** | The firm short name or \&quot;SNAM\&quot; | [optional] 
**relationship_code** | **str** | A system-generated code used for storage purposes | [optional] 
**logo_url** | **str** | Public URL of the firm&#x27;s logo | [optional] 
**disclosures** | **str** | HTML-encoded disclosures intended for reporting | [optional] 
**reporting_frequency** | **str** | See Frequency Codes | [optional] 
**report_on_heldaway_accounts** | **bool** | Option to include held-away assets in PDF reports | [optional] 
**show_bridge_logo** | **bool** | Show bridge logo? | [optional] 
**show_firm_logo** | **bool** | Show firm logo? | [optional] 
**cp_enabled** | **bool** | Is the client portal is enabled for the firm&#x27;s customers? | [optional] 
**cp_web_reports_enabled** | **bool** | Can clients access their own web reports from the portal? | [optional] 
**cp_printable_reports_enabled** | **bool** | Can clients download printable reports? | [optional] 
**cp_invoices_enabled** | **bool** | Can clients view their invoices? | [optional] 
**cp_shared_files_enabled** | **bool** | Can clients access shared files? | [optional] 
**cp_heldaways_enabled** | **bool** | Can clients access and add heldaway assets? | [optional] 
**invoice_header** | **str** | HTML invoice header | [optional] 
**invoice_footer** | **str** | HTML invoice footer | [optional] 
**invoice_from** | **str** | The address of the firm | [optional] 
**invoice_due_date_option** | **str** | Option to use for calculating due date. Choices are 30 (30 days from the invoice date), E (end of next month), or the empty string. | [optional] 
**invoice_include_fee_structures** | **bool** | Whether to include a description of the fee structures used in the billing | [optional] 
**invoice_effective_rates** | **bool** | Whether to include effective rates (total billed divided by total assets) in the invoice | [optional] 
**invoice_annualized_effective_rates** | **bool** | Whether to show the effective rate as an annual percentage | [optional] 
**invoice_show_agreement** | **bool** | Whether to show the disclaimer agreement text, standard from V2 invoices | [optional] 
**invoice_not_a_bill_explanation** | **bool** | If true and the invoice doesn&#x27;t represent a bill (because it&#x27;ll be withdrawn directly) | [optional] 
**is_active** | **bool** | Is the firm active? | [optional] 
**is_billing_active** | **bool** | Is the billing state active? | [optional] 
**billing_include_accrued_income** | **bool** | Is accrued income included? | [optional] 
**billing_partition_option** | **str** | See Frequency Codes | [optional] 
**primary_color** | **str** | Primary color is the main color used on Atlas | [optional] 
**accent_color** | **str** | Accent color is occasionally used in elements such as checkboxes | [optional] 
**brand_colors** | **list[str]** | Brand colors are used in charts generated from reporting | [optional] 
**created_at_utc** | **datetime** | Timestamp for when the record was created | [optional] 
**updated_at_utc** | **datetime** | Timestamp for when the record was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

