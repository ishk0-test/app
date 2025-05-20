from flask import Flask, send_file, abort
import os

# 200m
_dummy_allocation = bytearray(200 * 1024 * 1024)

app = Flask(__name__)

# data
FILE_PATH = os.path.join(os.path.dirname(__file__), 'data', 'archive.zip')

@app.route('/archive.zip')
def download_archive():
    if os.path.isfile(FILE_PATH):
        return send_file(FILE_PATH, as_attachment=True)
    else:
        abort(404)

if __name__ == '__main__':
    # 8080
    app.run(host='0.0.0.0', port=8080)
