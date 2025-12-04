import os
from datetime import datetime
from flask import Flask, render_template, request, url_for
import qrcode
from qrcode.constants import ERROR_CORRECT_H

app = Flask(__name__)

# Path to save QR images
QR_FOLDER = os.path.join("static", "qrs")
os.makedirs(QR_FOLDER, exist_ok=True)


def generate_qr_image(data: str, filename: str) -> str:
    """Generate a QR code PNG file."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save path (absolute)
    file_path = os.path.join(QR_FOLDER, filename)
    img.save(file_path)

    # Return only filename for url_for()
    return filename


@app.route("/", methods=["GET", "POST"])
def index():
    qr_image_filename = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("data", "").strip()

        if user_input:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
            filename = f"qr_{timestamp}.png"

            qr_image_filename = generate_qr_image(user_input, filename)

    return render_template("index.html",
                           qr_image_filename=qr_image_filename,
                           user_input=user_input)


if __name__ == "__main__":
    app.run(debug=True)
