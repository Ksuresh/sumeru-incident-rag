---
incident_id: INC-UNKNOWN-0011
date_reported: 
customer_name: Au bank
environment: Production
service_module: webapi
incident_category: Application
severity_level: P3
detected_by: Client
owner_resolver: 
incident_tags: 
linked_incidents: 
postmortem_link: 
gpt_insight_label: 
---

# Incident INC-UNKNOWN-0011

## Summary
Exceptions in webapi

## Impact Scope
Less

## Observability / Logs


## Root Cause (as recorded)
we identified one particular API (api/mvp/account/offline/myaccounts) that is being called repeatedly from the mobile app and returning a 400 status code, which mobile team have to analyse and minimize calling this API only when appropriate.

## Resolution Steps
Need to disable/verify that api from th code

## Detection & Resolution Timing
- Time to Detect (TTD): 15m
- Time to Resolve (TTR): 25m

## Preventive Actions


## Automation Suggestion

