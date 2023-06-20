# CASSI Report Follow-Up

## Problem

We need additional information to potentially explain the increased amount disengagements of autonomous mode.

## Hypothesis

We believe that inclement weather or crown cover could be contributing factors that could explain the increase in disengagements of autonomous mode.

## Potential Solutions

We have to map a weather condition onto the instances of disengagement.

1. We aggregade the autonomous-shuttle-disengagement.csv data to the closest hour and map the weather conditions onto the aggregate/groupby.
2. We map the weather conditions onto the closest onto each disengagement.

## Data Sources

- [CASSI Autonomous Shuttle Disengagement Dataset](https://data.townofcary.org/explore/dataset/autonomous-shuttle-disengagement/information/?disjunctive.cause&sort=incident_datetime)
- [Meteostat Hourly Weather Data API](https://dev.meteostat.net/python/hourly.html#hourly-data)
