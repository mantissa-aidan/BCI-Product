# DATA3888 - BCI Call Button - dev version



A project to create a call button for movement impaired persons. Uses a BYB spike box to track the users eye movements. 

Model training and prediction method is borrowed from [RichardLiuLiu](https://github.com/RichardLiuLiu/Spoken_Number_Recognition)

 - *NOTE:(this version currently works with voice data I recorded myself) We'll need to replace these recordings with our own.*
 - NOTE:*this also includes an implementation of the autoencoder*

## Installation
You will need a Python 3.6 installation.
With conda: 

**Create a new Python 3.6 environment:**
`conda create -n bci-environment python=3.6`
    
**Activate it:**

    conda activate bci-environment

   **Once the environment is activate**:
   

    (bci_environment) pip install --user --requirement requirements.txt

**Run:**
 `pip install -r requirements.txt` 

## Usage
### Running the pretrained model:
To run the pretrained model `python Recorder_GUI.py`
This will open a small interface:

<img src="https://i.imgur.com/MgCKC49.gif" width="300" height="200" />

Once the START button is pressed the app will wait for a word to be spoken, you will get best performance in an environment with as little background noise as possible.

When you speak the app will record a 1 second audio clip which it will then return a class probability "left" "right" "nothing" or "can't recognise".

**08/10/2019**
The model is currently trained on ~150 samples of left/right and nothing samples.  Since it was trained with my voice, it probably won't work for you.
Training performance can be seen [here](https://app.wandb.ai/z3467842/uncategorized?workspace=user-z3467842):

### Training your own model
TODO

## Improving Accuracy
TODO

## How it works
TODO
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzIxMTE2NjNdfQ==
-->