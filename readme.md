---


---

<h1 id="data3888---bci-call-button---dev-version">DATA3888 - BCI Call Button - dev version</h1>
<p>UPDATE: Final iteration here

<p>A project to create a call button for movement impaired persons. Uses a BYB spike box to track the users eye movements.</p>
<p>Model training and prediction method is borrowed from <a href="https://github.com/RichardLiuLiu/Spoken_Number_Recognition">RichardLiuLiu</a></p>
<ul>
<li><em>NOTE:(this version currently works with voice data I recorded myself) We’ll need to replace these recordings with our own.</em></li>
<li>NOTE:<em>this also includes an implementation of the autoencoder</em></li>
</ul>
<h2 id="installation">Installation</h2>
<p>You will need a Python 3.6 installation.<br>
With conda:</p>
<p><strong>Create a new Python 3.6 environment:</strong><br>
<code>conda create -n bci-environment python=3.6</code></p>
<p><strong>Activate it:</strong></p>
<pre><code>conda activate bci-environment
</code></pre>
<p><strong>Once the environment is activate</strong>:</p>
<pre><code>(bci_environment) pip install --user --requirement requirements.txt
</code></pre>
<p><strong>Run:</strong><br>
<code>pip install -r requirements.txt</code></p>
<h2 id="usage">Usage</h2>
<h3 id="running-the-pretrained-model">Running the pretrained model:</h3>
<p>To run the pretrained model <code>python Recorder_GUI.py</code><br>
This will open a small interface:</p>
<img src="https://i.imgur.com/MgCKC49.gif" width="300" height="200">
<p>Once the START button is pressed the app will wait for a word to be spoken, you will get best performance in an environment with as little background noise as possible.</p>
<p>When you speak the app will record a 1 second audio clip which it will then return a class probability “left” “right” “nothing” or “can’t recognise”.</p>
<p><strong>08/10/2019</strong><br>
The model is currently trained on ~150 samples of left/right and nothing samples.  Since it was trained with my voice, it probably won’t work for you.<br>
Training performance can be seen <a href="https://app.wandb.ai/z3467842/uncategorized?workspace=user-z3467842">here</a>:</p>
<h3 id="training-your-own-model">Training your own model</h3>
<p>TODO</p>
<h2 id="improving-accuracy">Improving Accuracy</h2>
<p>TODO</p>
<h2 id="how-it-works">How it works</h2>
<p>TODO</p>

