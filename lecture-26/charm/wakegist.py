import argparse
import os
from datetime import datetime
from threading import Thread

import numpy as np
import pvporcupine
import soundfile
from pvrecorder import PvRecorder

keywords = ["jarvis"]
keyword_paths = [pvporcupine.KEYWORD_PATHS[x] for x in keywords]
sensitivities = [.5]

porcupine = None
recorder = None
try:
            porcupine = pvporcupine.create(
                library_path=pvporcupine.LIBRARY_PATH,
                model_path=pvporcupine.MODEL_PATH,
                keyword_paths=keyword_paths,
                sensitivities=sensitivities)

            recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
            recorder.start()

            print(f'Using device: {recorder.selected_device}')

            print('Listening {')
            for keyword, sensitivity in zip(keywords, sensitivities):
                print('  %s (%.2f)' % (keyword, sensitivity))
            print('}')

            while True:
                pcm = recorder.read()

                result = porcupine.process(pcm)
                if result >= 0:
                    print('[%s] Detected %s' % (str(datetime.now()), keywords[result]))


except KeyboardInterrupt:
    print('Stopping ...')
finally:
    if porcupine is not None:
        porcupine.delete()
