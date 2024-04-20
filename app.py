from flask import Flask, request, render_template
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    data = request.form.to_dict()
    data_json = json.dumps(data)
 
    try:
        # Run the script and capture the output
        result = subprocess.run(['python', 'Timetable/src/driver.py', data_json], capture_output=True, text=True)
        output = result.stdout.strip()  # Get the output and remove leading/trailing whitespace

        # Parse the output to extract schedule information
        schedule_info = []
        lines = output.split('\n')
        is_schedule_section = False

        for line in lines:
            if 'Class #' in line:
                is_schedule_section = True
            elif is_schedule_section and line.strip():  # Check if it's a non-empty line in the schedule section
                parts = [part.strip() for part in line.split('  ') if part.strip()]  # Split and clean parts
                if len(parts) == 6:  # Ensure we have all expected parts
                    schedule_info.append({
                        'Class #': parts[0],
                        'Dept': parts[1],
                        'Course': parts[2],
                        'Room': parts[3],
                        'Instructor': parts[4],
                        'Meeting Time': parts[5]
                    })

        if schedule_info:
            return render_template('schedule.html', schedule_info=schedule_info)
        else:
            return 'Error: Schedule information not found or invalid format.'

    except Exception as e:
        return f'Error executing script: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
