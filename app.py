from flask import Flask, render_template, request, redirect, url_for
import os
from modules.preprocessing import preprocess_document
from modules.ocr import extract_text
from modules.verification import verify_data
from modules.analytics import generate_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('error.html', message="No file uploaded.")
    file = request.files['file']
    if file.filename == '':
        return render_template('error.html', message="No file selected.")
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        try:
            # Step 1: Preprocess the document
            processed_image = preprocess_document(file_path)
            # Step 2: Extract text using OCR
            extracted_text = extract_text(processed_image)
            # Step 3: Verify extracted data
            verification_result = verify_data(extracted_text)
            # Step 4: Generate analytics report
            generate_report([{'Category': 'Documents Processed', 'Count': 1}])

            return render_template('result.html', result=verification_result, text=extracted_text)
        except Exception as e:
            return render_template('error.html', message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
