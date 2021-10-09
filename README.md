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
_Fitbit's Data Export Tool gives the following_
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
