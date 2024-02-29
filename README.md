## Simple-Augmentor

Welcome to the image augmentor created by Aditya Siddharth Jyoti!

**What is Image Augmentation?**

Image augmentation is a powerful technique in computer vision that artificially expands the size and diversity of a training dataset. This is crucial for deep learning models, which require vast amounts of data to excel.

**Why Use Image Augmentation?**

* **Increases Data Volume:** Artificially creates new data from existing images, which is especially useful when working with limited datasets.
* **Reduces Overfitting:** Prevents the model from memorizing specific training data details, leading to better performance on unseen data.
* **Improves Generalization:** Helps the model recognize the same object/concept under various conditions like different lighting, angles, and positions.
* **Enhances Model Robustness:** Makes the model less susceptible to variations in real-world data, leading to improved performance.

**How to Access This Augmentor**

**Globally:**

Visit the following link 

`(https://aditya-augmentor.onrender.com/)`

(![Display of website](https://github.com/arch-adi21/Simple-Augmentor/assets/155255348/5fc55ec2-9e14-4420-9da7-22ab9da099dc)


**Locally:**

1. **Download the repository:**
   - Go to the Simple-Augmentor repository on GitHub.
   - Click "Code" and then "Download ZIP".

2. **Install dependencies:**
   - Open a terminal or command prompt in the downloaded folder.
   - Run the following command to install required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

3. **Run the server locally:**
   - In the terminal, run the following command to start the production server:

     ```bash
     gunicorn app:app
     ```

