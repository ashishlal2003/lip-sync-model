# Lip Sync Model

This project aims to develop a model that synchronizes lip movements in images based on the provided text input (words or phrases). The model leverages the MIRACL dataset, which contains a variety of images depicting individuals speaking specific words and phrases.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The objective of this project is to build a two-step CNN-RNN architecture. The CNN will be used for feature extraction from images, and the RNN (LSTM) will model the temporal patterns of lip movements corresponding to the text input. 

## Dataset

The project utilizes the **MIRACL dataset**, which includes:

- Color images and depth images of male and female speakers.
- A total of 10 speakers, each uttering 10 different words and phrases.
- Frames corresponding to specific words, which will be used to train the model.

### Data Preprocessing

1. Images are cropped to focus on facial regions using Haar cascade face detection.
2. Images are resized to 224x224 pixels for input into the pre-trained VGGFace model.
3. The data will be split into training, validation, and test sets to evaluate model performance.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/lip-sync-model.git
   cd lip-sync-model

2. Install the required packages:
   ```bash
   pip install -r requirements.txt

3. Setup the .env file from the provided template:
   ```bash
   cp .env.sample .env

## Usage

1. Download the MIRACL dataset from the [official website](https://sites.google.com/site/achrafbenhamadou/-datasets/miracl-vc1).

2. In the ```.env``` file, set the path to the dataset:
   ```bash
   DATASET_PATH=/path/to/miracl-dataset

3. To preprocess the data, run the following command:
   ```bash
   python src/preprocess_data.py

4. To train the model, run the following command:
   ```bash
    python src/model.py

5. To evaluate the model, run the following command:
   ```bash
   python src/evaluate.py

## Project Structure

The project structure is as follows:

```
lip-sync-model/
├── notebooks/         # Jupyter notebooks for exploration
├── src/              # Python modules for the main application
│   ├── preprocessing.py
│   ├── model.py
│   └── training.py
├── requirements.txt   # List of dependencies
├── README.md          # Project overview
├── .env.sample        # Template for environment variables
└── .gitignore         # Files and directories to ignore
```

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Implement the changes.
4. Send a pull request.