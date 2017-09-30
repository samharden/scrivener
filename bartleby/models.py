from __future__ import unicode_literals
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import StringIO, BytesIO
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from django.db import models
import os
# Create your models here.
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import pyaudio
from django.utils import timezone
import datetime
cwd = os.getcwd()

from django.db import models

class RecordForm(models.Model):
    file_name = models.CharField(max_length=20)

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

def bartleby_get(file_name):

    speech_to_text = SpeechToTextV1(
        username='username',
        password='password',
        x_watson_learning_opt_out=False
    )

    # print(json.dumps(speech_to_text.models(), indent=2))
    #
    # print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))
    os.chdir(cwd+'/bartleby/audio/')
    with open(join(dirname(__file__), file_name+'.wav'),
              'rb') as audio_file:
        speech_data = json.dumps(speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            word_confidence=True, speaker_labels=True, continuous=True),
            indent=2)


    data = speech_data
    print(data)
    data = json.loads(data)

    data = data["results"][0]["alternatives"][0]["transcript"]

    return data

def write_transcript_to_pdf(data, file_name):

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
