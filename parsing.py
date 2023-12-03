import pandas as pd
from enum import Enum

class WorkoutColumns(str, Enum):
    date = "Date"
    workout_name = "Workout Name"
    duration = "Duration"
    exercise_name = "Exercise Name"
    set_order = "Set Order"
    weight = "Weight"
    reps = "Reps"
    distance = "Distance"
    seconds = "Seconds"
    notes = "Notes"
    workout_notes = "Workout Notes"
    rpe = "RPE"

workout_df = pd.read_csv("strong.csv")
most_recent_date: str = workout_df[WorkoutColumns.date].max()
most_recent_workout: pd.DataFrame = workout_df[workout_df[WorkoutColumns.date] == most_recent_date]

first_row: pd.Series = most_recent_workout.iloc[0]
workout_name: str = first_row[WorkoutColumns.workout_name]
duration: str = first_row[WorkoutColumns.duration]

unique_exercises = most_recent_workout[WorkoutColumns.exercise_name].unique()

exercises = []

for exercise in unique_exercises:
    exercise_df = most_recent_workout[most_recent_workout[WorkoutColumns.exercise_name] == exercise]
    num_sets = exercise_df.shape[0]
    max_weight = exercise_df[WorkoutColumns.weight].max()
    best_sets = exercise_df[exercise_df[WorkoutColumns.weight] == max_weight]
    best_set_reps = best_sets[WorkoutColumns.reps].max()
    
    exercises.append({
        "name": exercise,
        "sets": num_sets,
        "best_set_weight": max_weight,
        "best_set_reps": best_set_reps
    })

data = {
    "date": most_recent_date,
    "workout_name": workout_name,
    "duration": duration,
    "exercises": exercises
}

print(data)