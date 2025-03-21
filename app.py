from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Directory to store QR code images
qr_folder = 'qr_images'
if not os.path.exists(qr_folder):
    os.makedirs(qr_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Get the data from the form
    data = request.form['data']
    
    # Generate QR code
    img = qrcode.make(data)
        
    # Save the QR code image
    img_path = os.path.join(qr_folder, 'qrcode.png')
    img.save(img_path)
    
    # Send the image file to the client
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
