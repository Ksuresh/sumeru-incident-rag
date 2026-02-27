---
incident_id: INC-UNKNOWN-0008
date_reported: 
customer_name: Equitas
environment: Production
service_module: MSMQ
incident_category: Application
severity_level: P1
detected_by: PS Team and Client
owner_resolver: 
incident_tags: Code,deployment
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0008

## Summary
queue building up in collection batch endpoint

## Impact Scope
queue processing will be slow due to high trafic

## Observability / Logs


## Root Cause (as recorded)
since its calling thrid party api which responding slow has resulted slow processing of queues

## Resolution Steps
removed the thridparty api to another endpoint  which is used only for the call or send data using the this api

## Detection & Resolution Timing
- Time to Detect (TTD): 8hr
- Time to Resolve (TTR): 48hrs

## Preventive Actions
need to make sure all the thrid party endpoints should be called using the seprate endpoint

## Automation Suggestion
No
