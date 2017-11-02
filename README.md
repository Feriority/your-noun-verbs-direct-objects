# your-noun-verbs-direct-objects

Inspired by https://twitter.com/feardragon64/status/924103536824131585

## Setup

I'll try to streamline this once everything works, but for now setup is a little messy.
You'll need to install on your own: python 3, virtualenv, pyaudio

This assumes your default python is python 3; if it isn't, pass `--python=python3` to virtualenv.
`virtualenv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

You'll also need to download some nltk data packages.  You can do this interactively using ipython (already installed if you've followed setup so far):
`ipython`
`import nltk; nltk.download()`

From the interactive downloader, download `punkt` and `averaged_perceptron_tagger`.

## Useful documentation

[speech_recognition](https://github.com/Uberi/speech_recognition)
[nltk](http://www.nltk.org/)
