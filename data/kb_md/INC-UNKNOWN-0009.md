---
incident_id: INC-UNKNOWN-0009
date_reported: 
customer_name: DBS
environment: Production
service_module: MSMQ
incident_category: Service
severity_level: P1
detected_by: PS Team and Client
owner_resolver: 
incident_tags: 
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0009

## Summary
queues are not moving

## Impact Scope
ALL Users

## Observability / Logs


## Root Cause (as recorded)
quota got full for MSMQ

## Resolution Steps
need to increase the quota for msmq

## Detection & Resolution Timing
- Time to Detect (TTD): 30m
- Time to Resolve (TTR): 72hrs

## Preventive Actions
need to check the quota frequently and clear the dead letter queues

## Automation Suggestion
no
