from flask import Flask, request, render_template, send_file, session
from flask_session import Session
import pandas as pd
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_generated_secret_key'  # Replace with your generated secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def compare_files(file1, file2, file_type1, file_type2):
    if file_type1 == 'csv':
        df1 = pd.read_csv(file1)
    else:
        df1 = pd.read_excel(file1)

    if file_type2 == 'csv':
        df2 = pd.read_csv(file2)
    else:
        df2 = pd.read_excel(file2)

    differences = df1.compare(df2)
    return differences

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        export_name = request.form.get('export_name', 'differences')

        if action == 'upload':
            file1 = request.files.get('file1')
            file2 = request.files.get('file2')

            if file1 and file2:
                try:
                    file_type1 = file1.filename.split('.')[-1]
                    file_type2 = file2.filename.split('.')[-1]
                    session['file1'] = file1.read()
                    session['file2'] = file2.read()
                    session['file_type1'] = file_type1
                    session['file_type2'] = file_type2

                    file1.seek(0)
                    file2.seek(0)
                    file1_data = io.BytesIO(file1.read())
                    file2_data = io.BytesIO(file2.read())
                    differences = compare_files(file1_data, file2_data, file_type1, file_type2)
                    if differences is not None:
                        diff_html = differences.to_html()
                        return render_template('result.html', diff_html=diff_html, export_name=export_name)
                    else:
                        return "No differences found."
                except Exception as e:
                    return f"Error: {e}"

        elif action == 'export':
            if 'file1' in session and 'file2' in session:
                try:
                    file_type1 = session.get('file_type1')
                    file_type2 = session.get('file_type2')
                    file1_data = session['file1']
                    file2_data = session['file2']

                    if file_type1 == 'csv':
                        file1 = io.StringIO(file1_data.decode('utf-8'))
                    else:
                        file1 = io.BytesIO(file1_data)

                    if file_type2 == 'csv':
                        file2 = io.StringIO(file2_data.decode('utf-8'))
                    else:
                        file2 = io.BytesIO(file2_data)

                    differences = compare_files(file1, file2, file_type1, file_type2)
                    
                    if differences is not None:
                        csv_io = io.StringIO()
                        differences.to_csv(csv_io)
                        csv_io.seek(0)
                        return send_file(
                            io.BytesIO(csv_io.getvalue().encode('utf-8')),
                            mimetype='text/csv',
                            download_name=f'{export_name}.csv',
                            as_attachment=True
                        )
                    else:
                        return "No differences found."
                except Exception as e:
                    return f"Error: {e}"
            else:
                return "No files found in session."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
