import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

habits = ["Test Habit", "Test habit 2"]  # List of habits

def date_range(start: datetime.date):
    dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
    return dates

@app.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()
    print(selected_date)
    
    return render_template("index.html", 
                           habits=habits, 
                           title="Habit Tracker - Home", 
                           date_range=date_range, 
                           selected_date=selected_date
                           )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
            
    return render_template("add_habit.html", title="Habit Tracker - Add Habit")
