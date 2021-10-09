# fitport
Making my old Fitbit Data useful again.
___

## Goals
1. Port Fitbit Data to Apple Health
   - [ ] Weight
   - [ ] Sleep
   - [ ] Resting HR
   - [ ] Demographic VO2 Max
   - [ ] Steps
   - [ ] Workouts
2. Create Unified Database of all Health Data
3. Make Pretty Graphs
___
## Data Structure
_Fitbit Data Export Tool gives the following_
```text
data/user-site-export
├── altitude
├── calories
├── demographic_vo2_max
├── distance
├── exercise
├── heart_rate
├── lightly_active_minutes
├── moderately_active_minutes
├── resting_heart_rate
├── run_vo2_max
├── sedentary_minutes
├── sleep
├── steps
├── time_in_heart_rate_zones
├── very_active_minutes
└── weight
```
___
## Step 1: Weight & BMI
```json5
{
  // Example Weight Record
  "logId" : 1431993599000,
  "weight" : 191.8, // weight in pounds
  "bmi" : 27.77,
  "date" : "05/18/15", // MM/DD/YY
  "time" : "23:59:59"
}
```
**Shortcuts Weight Health Sample**
![Shortcuts Weight Entry](media/shortcuts-weight-entry.png)

**Shortcuts Weight Health Sample**
![Shortcuts Body Mass Index](media/shortcuts-bmi-entry.png)

___
## Step 2: Sleep
```json5
// Example Sleep Record
{
  "logId" : 1028309330,
  "dateOfSleep" : "2015-06-16",
  "startTime" : "2015-06-15T23:46:00.000",
  "endTime" : "2015-06-16T10:19:10.000",
  "duration" : 37980000,
  "minutesToFallAsleep" : 7,
  "minutesAsleep" : 608,
  "minutesAwake" : 18,
  "minutesAfterWakeup" : 0,
  "timeInBed" : 633,
  "efficiency" : 97,
  "type" : "classic",
  "infoCode" : 0,
  "levels" : {
    "summary" : {
      "restless" : {
        "count" : 14,
        "minutes" : 24
      },
      "awake" : {
        "count" : 1,
        "minutes" : 1
      },
      "asleep" : {
        "count" : 0,
        "minutes" : 608
      }
    },
    "data" : [{
      "dateTime" : "2015-06-15T23:46:00.000",
      "level" : "restless", // restless, asleep, awake
      "seconds" : 360
    }, {
      "dateTime" : "2015-06-15T23:52:00.000",
      "level" : "awake", // restless, asleep, awake
      "seconds" : 60
    }]
  },
  "mainSleep" : true
}
```
**Shortcuts Sleep Entry**
![Shortcuts Sleep Entry](media/shortcuts-sleep-entry.png)
```
Type: Sleep
Value: [ Awake, In Bed, Asleep ]
Start Date: ...
End Date: ...
```