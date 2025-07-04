import os
from flask import Flask, request, jsonify, render_template, send_file
from dotenv import load_dotenv
import traceback
import subprocess
import uuid

load_dotenv()

app = Flask(__name__)

DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER", "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    try:
        data = request.get_json(force=True)
        url = data.get("url")
        format = data.get("format", "mp4")

        if not url:
            return jsonify({"error": "No URL provided"}), 400

        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        temp_id = str(uuid.uuid4())[:8]
        output_template = os.path.join(DOWNLOAD_FOLDER, f"{temp_id}.%(ext)s")

        command = ["yt-dlp", "-o", output_template]

        if format == "mp3":
            command += [
                "--extract-audio",
                "--audio-format", "mp3",
                "--audio-quality", "0"
            ]
        else:
            command += ["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4"]

        command.append(url)
        print("Running command:", " ".join(command))

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print("yt-dlp exited with error, continuing...")

        for file in os.listdir(DOWNLOAD_FOLDER):
            if file.startswith(temp_id):
                file_path = os.path.join(DOWNLOAD_FOLDER, file)
                print(f"Sending file: {file_path}")
                return send_file(file_path, as_attachment=True)

        return jsonify({"error": "Download failed or file not found"}), 500

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
