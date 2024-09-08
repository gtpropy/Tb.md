import os
from flask import Blueprint, request, redirect, url_for, send_from_directory, flash, jsonify, current_app

# Initialize the Blueprint
image_upload_bp = Blueprint('image_upload', __name__)

# Allowed file extensions for images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# Helper function to check if a file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route to upload images
@image_upload_bp.route('/upload_asset', methods=['POST'])
def upload_image():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # If the user does not select a file
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # If the file is allowed
    if file and allowed_file(file.filename):
        filename = file.filename
        upload_folder = current_app.config['UPLOAD_FOLDER']
        file.save(os.path.join(upload_folder, filename))
        return jsonify({"message": "Image uploaded successfully!", "filename": filename}), 201

    return jsonify({"error": "File extension not allowed"}), 400


# Route to list all uploaded images
@image_upload_bp.route('/uploads', methods=['GET'])
def list_uploaded_files():
    upload_folder = current_app.config['UPLOAD_FOLDER']
    files = os.listdir(upload_folder)
    return jsonify({"files": files}), 200


# Route to serve uploaded images
@image_upload_bp.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    upload_folder = current_app.config['UPLOAD_FOLDER']
    if not os.path.exists(os.path.join(upload_folder, filename)):
        return jsonify({"error": "File not found"}), 404
    return send_from_directory(upload_folder, filename)
