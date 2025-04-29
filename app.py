from flask import Flask, render_template, redirect
import pandas as pd

app = Flask(__name__)

def load_events():
    df = pd.read_csv('tonight.csv')
    events = df.to_dict(orient='records')
    return events

def save_events(events):
    df = pd.DataFrame(events)
    df.to_csv('tonight.csv', index=False)

@app.route('/')
def index():
    events = load_events()
    return render_template('index.html', events=events)

@app.route('/vote/<int:event_id>', methods=['POST'])
def vote(event_id):
    events = load_events()
    for event in events:
        if event['event_id'] == event_id:
            event['votes'] += 1
            break
    save_events(events)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    