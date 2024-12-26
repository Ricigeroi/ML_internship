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
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



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

    files = request.files.getlist('file')
    responses = []

    for file in files:
        if file.filename == '':
            responses.append({"filename": None, "error": "No file selected"})
            continue

        if not allowed_file(file.filename):
            responses.append({"filename": file.filename, "error": "File type not allowed"})
            continue

        try:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_DIRECTORY, filename)

            if os.path.exists(file_path):
                responses.append({"filename": filename, "error": "File already exists"})
                continue

            file.save(file_path)
            responses.append({"filename": filename, "message": "File uploaded successfully"})
        except Exception as e:
            responses.append({"filename": file.filename, "error": f"Failed to save the file: {str(e)}"})

    return jsonify(responses), 207


@app.route('/files/<name>', methods=['DELETE'])
def delete_file(name):
    try:
        os.remove(os.path.join(UPLOAD_DIRECTORY, name))
        return jsonify({"message": "File deleted successfully"}), 200
    except Exception as e:
        return make_response(jsonify({"error": f"Failed to delete file: {str(e)}"}), 409)


if __name__ == '__main__':
    app.run()
