from flask import Flask, request, render_template, send_file
import pandas as pd
import io

app = Flask(__name__)

def compare_sheets(file, sheet_name1, sheet_name2):
    df = pd.read_excel(file, sheet_name=None)
    if sheet_name1 in df and sheet_name2 in df:
        sheet1 = df[sheet_name1]
        sheet2 = df[sheet_name2]
        differences = sheet1.compare(sheet2)
        differences = differences.fillna('')  # Replace NaN with empty strings

        return differences
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        sheet_name1 = request.form.get('sheet1')
        sheet_name2 = request.form.get('sheet2')
        action = request.form.get('action')
        export_name = request.form.get('export_name', 'differences')  # Default name if not provided

        if file and sheet_name1 and sheet_name2:
            try:
                excel_file = io.BytesIO(file.read())
                differences = compare_sheets(excel_file, sheet_name1, sheet_name2)

                if differences is not None:
                    if action == 'compare':
                        diff_html = differences.to_html()
                        return render_template('result.html', diff_html=diff_html, export_name=export_name)
                    elif action == 'export':
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
                    return "Sheets not found in the Excel file."
            except Exception as e:
                return f"Error: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
