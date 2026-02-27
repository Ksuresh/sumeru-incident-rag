---
incident_id: INC-UNKNOWN-0007
date_reported: 
customer_name: Equitas
environment: Production
service_module: MSMQ
incident_category: Application
severity_level: P1
detected_by: PS Team and Client
owner_resolver: PS team
incident_tags: config files
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0007

## Summary
queue building up

## Impact Scope
queue processing will be slow due to high trafic

## Observability / Logs
queue got struck

## Root Cause (as recorded)
MAX Corn is mentioned as 1 in feedback and other endpoints

## Resolution Steps
max corn has been changed to 3, which has resulted in queue processing quickly

## Detection & Resolution Timing
- Time to Detect (TTD): 15m
- Time to Resolve (TTR): 25m

## Preventive Actions
Need to check all the confuguration before and after deployment

## Automation Suggestion
Yes
