from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from bartleby.templates import *
import os
from django import forms
import watson_developer_cloud
from bartleby.forms import *
from bartleby.models import bartleby_get, write_transcript_to_pdf
import json
import pyaudio
import wave
import logging
logger = logging.getLogger(__name__)
cwd = os.getcwd()

def index(request):
    form = RecordForm()
    if request.method == 'POST':
        print("Hello")
        form = RecordForm(request.POST)

        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = 20
            WAVE_OUTPUT_FILENAME = file_name+".wav"

            p = pyaudio.PyAudio()
            info = p.get_host_api_info_by_index(0)
            numdevices = info.get('deviceCount')
            for i in range(0, numdevices):
                    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

            # p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* recording")

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* done recording")

            stream.stop_stream()
            stream.close()
            p.terminate()
            os.chdir(cwd+'/bartleby/audio/')
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)

            wf.writeframes(b''.join(frames))
            wf.close()

            data = bartleby_get(cwd+'/bartleby/audio/'+file_name)
            print('Helloooooo')
            messages.success(request, data)
            print(data)


            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % file_name
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer,
                                    pagesize=letter,
                                    rightMargin=72,leftMargin=72,
                                    topMargin=72,bottomMargin=50)
            document=[]

            styles=getSampleStyleSheet()
            styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
            respondent_text = '<font size=12> <style="justify"> <b> %s\
                    </b></style></font>' % data

            document.append(Paragraph(respondent_text, styles["Justify"]))
            doc.build(document)
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response


        else:
            form = RecordForm()
    return render(request, 'bartleby/index.html', {'form':form})
