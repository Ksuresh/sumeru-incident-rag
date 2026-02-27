---
incident_id: INC-UNKNOWN-0014
date_reported: 
customer_name: MT
environment: Production
service_module: Harddisk
incident_category: Hardware
severity_level: P1
detected_by: Infra Team
owner_resolver: infra
incident_tags: DISK
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0014

## Summary
C drive is full

## Impact Scope
file are not getting saved in that drive

## Observability / Logs
Disk full

## Root Cause (as recorded)
windows patches and database files size is high which has resulted in c drive full

## Resolution Steps
Increased the size of c drive

## Detection & Resolution Timing
- Time to Detect (TTD): 15m
- Time to Resolve (TTR): 25m

## Preventive Actions
increased the threshold levels to 85 %

## Automation Suggestion
No
