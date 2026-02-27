---
incident_id: INC-UNKNOWN-0010
date_reported: 
customer_name: DBS
environment: Production
service_module: MSMQ
incident_category: Service
severity_level: P2
detected_by: PS Team and Client
owner_resolver: 
incident_tags: 
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0010

## Summary
queues are not moving  for feedback endpoint

## Impact Scope
queue processing will be slow due to high trafic

## Observability / Logs


## Root Cause (as recorded)
third party api is not responding

## Resolution Steps
disable this feature from the application and made console application push th data

## Detection & Resolution Timing
- Time to Detect (TTD): 30m
- Time to Resolve (TTR): 72hrs

## Preventive Actions
need to check the quota frequently and clear the dead letter queues

## Automation Suggestion

