from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import Augmentor
import shutil
import os
from imgaug import augmenters as iaa
import cv2

app = Flask(__name__, static_url_path='/static')

PROJECT_FOLDER = os.path.expanduser('~/Desktop/AugmentationApp')
UPLOAD_FOLDER = os.path.join(PROJECT_FOLDER, 'static/uploads')
AUGMENTED_FOLDER = os.path.join(PROJECT_FOLDER, 'static/augmented_images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def augment_images(input_path, output_path, num_augmented_images=5):
    # Ensure the output path exists
    os.makedirs(output_path, exist_ok=True)
    print('done step 1')

    # List all image files in the input path
    image_files = [f for f in os.listdir(input_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    print('done step 2')

    # Define augmentation pipeline
    seq = iaa.Sequential([
        iaa.Fliplr(0.5),  # Adjust probability for random horizontal flip
        iaa.GaussianBlur(sigma=(0.0, 3.0)),  # Random blur with varying strength
        iaa.Affine(rotate=(-45, 45), scale=(0.8, 1.2)),  # Random rotation and scaling
        iaa.AdditiveGaussianNoise(scale=(0, 0.05*255)),  # Random Gaussian noise
        iaa.WithBrightnessChannels(
    iaa.Add((-50, 50)), from_colorspace=iaa.CSPACE_BGR),
    iaa.GammaContrast((0.5, 2.0))
    ])
    print('done step 3')

    for image_file in image_files:
        # Load the image
        image_path = os.path.join(input_path, image_file)
        image = cv2.imread(image_path)
        print('done step 4')

        # Apply augmentation to create multiple augmented images
        augmented_images = [seq.augment_image(image) for _ in range(num_augmented_images)]
        print('done step 5')

        # Save augmented images to the output path
        base_name, ext = os.path.splitext(image_file)
        for i, augmented_image in enumerate(augmented_images):
            output_file = f"output{i+1}{ext}"
            output_file_path = os.path.join(output_path, output_file)
            cv2.imwrite(output_file_path, augmented_image)
        print('done step 6')

def clear_folders():
    # Clear contents of augmented_images folder
    if os.path.exists(AUGMENTED_FOLDER):
        shutil.rmtree(AUGMENTED_FOLDER)
    os.makedirs(AUGMENTED_FOLDER)

    # Clear contents of uploads folder
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    clear_folders() 
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    clear_folders() 
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        count = int(request.form['count'])

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = os.path.join(UPLOAD_FOLDER, 'input.jpg')
            file.save(filename)

            augment_images(UPLOAD_FOLDER, AUGMENTED_FOLDER, count)
            print('done step 0')

            return redirect(url_for('output'))

    return render_template('index.html')

@app.route('/output')
def output():
    augmented_images = os.listdir(AUGMENTED_FOLDER)
    return render_template('output.html', images=augmented_images)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(AUGMENTED_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)