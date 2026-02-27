---
incident_id: INC-UNKNOWN-0005
date_reported: 
customer_name: BOB
environment: Production
service_module: rabbitmq service
incident_category: Infrastructure issue
severity_level: P1
detected_by: PS Team and Client
owner_resolver: 
incident_tags: 
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0005

## Summary
rabbitmq service is down due to memory peaking

## Impact Scope
ALL Users

## Observability / Logs


## Root Cause (as recorded)
due to memory peaking, iis worker process for webapi , account endpoint consumeing high memory

## Resolution Steps
started the service of the w3wp, restart iis, endpoint and all other required services

## Detection & Resolution Timing
- Time to Detect (TTD): 15m
- Time to Resolve (TTR): 25m

## Preventive Actions


## Automation Suggestion

