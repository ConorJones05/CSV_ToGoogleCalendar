FROM python:3.9

ADD main.py .

ADD converter.py . 

RUN pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
 
CMD ["python", "./main.py"]