import json

goals_data = [ {"goal": "Squat 100kg", "due_date": "2025-03-20", "importance": "High", "remarks": "Progressive overload", "status": "In Progress", "category": "fitness"}, {"goal": "2.4km run under 10 mins", "due_date": "2025-04-01", "importance": "High", "remarks": "Interval training", "status": "Not Started", "category": "fitness"}, {"goal": "Submit project report", "due_date": "2025-03-15", "importance": "Medium", "remarks": "Proofread before submission", "status": "Not Started", "category": "work"}, {"goal": "Call family", "due_date": "2025-02-25", "importance": "Low", "remarks": "Weekly check-in", "status": "Completed", "category": "personal"} ]
goals_json = json.dumps(goals_data)
print(goals_json)

