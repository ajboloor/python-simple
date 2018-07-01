def text_to_speech(phrase):
    """Synthesize speech from text"""

    import pyttsx
    engine = pyttsx.init()
    engine.say(phrase)
    engine.runAndWait()


text = 'The quick brown fox jumped over the lazy dog.'
text_to_speech(text)
