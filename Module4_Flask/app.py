import os
from flask import Flask
from flask import request, abort, jsonify, send_from_directory, make_response
from werkzeug.utils import secure_filename


UPLOAD_DIRECTORY = 'files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json'}

# create dir if it's not exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/files', methods=['GET'])
def get_files():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route('/files/<name>', methods=['GET'])
def download_file(name):
    try:
        return send_from_directory(app.config['UPLOAD_DIRECTORY'], name, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/files', methods=['POST'])
def post_files():
    if 'file' not in request.files:
        return make_response(jsonify({"error": "No file part in the request"}), 400)

    file = request.files['file']

    if file.filename == '':
        return make_response(jsonify({"error": "No file selected"}), 400)

    if not allowed_file(file.filename):
        return make_response(jsonify({"error": "File type not allowed"}), 415)

    try:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_DIRECTORY, filename))
    except Exception as e:
        return make_response(jsonify({"error": f"Failed to save the file: {str(e)}"}), 500)

    return jsonify({"message": "File uploaded successfully", "filename": filename}), 201

if __name__ == '__main__':
    app.run()
