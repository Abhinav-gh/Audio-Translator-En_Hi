
# Audio Translation En-Hi
### Description
This project demonstrates an **end-to-end** pipeline for translating spoken English into spoken Hindi, preserving the *punctuation* and *pauses* of the *original* English audio.


### Brief Working
It involves several key steps: 
- Transcribing English audio into english text
- Punctuating the transcribed English text
- Translating the punctuated English text into Hindi text.
- Generating Hindi speech from the translated text
- Maintaining the original pauses in the final Hindi audio output.

## Demo
Please find the 2 demo files for this project:
- Input file given (English audio): https://github.com/Abhinav-gh/Audio-Translator-En_Hi/blob/main/shotcutLesson.wav
- Output file generated (Hindi audio): https://github.com/Abhinav-gh/Audio-Translator-En_Hi/blob/main/end_result_slow_output.wav
- The program also generates text since we are using speech to text models as well. So, we have **text** for both English and Hindi audio.

P.S. The output file generated is to be played at 1.25x for best results.
## Run on Collab
You can run this project on the **google collab**. However I would suggest to run it locally. 

Here is the link to my collab notebook: [click here](https://colab.research.google.com/drive/1rNpAC9WeqaSOIHpL7TT1wh3ryJ4kutIq?usp=sharing)
## Step-by-Step Installation to Run Locally

### Prerequisites

Before you start, ensure you have the following installed on your machine:

- **Python 3.7 or higher**
- **pip** (Python package installer)
---

#### 1. Clone the Repository

Clone the remote repository and cd into it
- Using SSH:
```bash
git clone git@github.com:Abhinav-gh/Audio-Translator-En_Hi.git
cd audio-translation-punctuation
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to manage the dependencies for this project. Use the following commands to create and activate a virtual environment:

- Virtual Environment using virtualenv
```bash
virtualenv env_name
```
- Activate the virtual environment
```bash
source env_name/bin/activate  # On Windows:\env_name\Scripts\activate

```
Refer to: https://virtualenv.pypa.io/en/latest/user_guide.html for more details

### 3. Installing dependencies
Install the required Python packages listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 4. Installing additional dependencies
> Install pytorch, torchvision and torchaudio
- Using CPU support only:
```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

```
- Using GPU support 
```bash
pip install torch torchvision torchaudio
```

### 5. Downloading pretrained models
I have **2** python scripts for the **2 models** that need to be downloaded and saved to your device
- Create 2 new directories: mbart_model and mms-tts-hin

```bash
mkdir mbart_model mms-tts-hin
```
- Navigate into the folder where the  scripts are stored
```bash
cd 'Model Download and Testing'
```
#### 1. Download mbart
This model will require approximately 2.4G of space on your drive
```bash
python3 download_mbart.py
```
#### 2. Download mms-tts-hin
```bash
python3 download_mms-tts-hin.py
```

### 6. Source audio and final steps
Place the source audio (.wav file) which is in English and you want to translate to Hindi under the project directory

- If you just did step 5. Make sure you are in the project directory
```bash
cd ..
```
- Add the source audio here as a .wav file
- Also create a dir for sessionFiles
```bash
mkdir sessionFiles
```
---
- [x]  Setup Finished
---
### Run!
Always do this to clear the sessionFiles before you run the app:
- Clear the sessionFiles
```bash
python3 clear_sessionFiles.py
```

Now we are good to go. Run the code:
```bash
python3 english_to_hindi_v2.py
```

You should see a file named: **end_result_slow_output.wav** under the project directory. Please play this file at 1.25x speed for correct results.

Several other .wav audio files will be generated under ./sessionFiles. You can delete them. Run **clear_sessionFiles.py** as mentioned above


## Authors

- [@Abhinav-gh](https://www.github.com/Abhinav-gh)

