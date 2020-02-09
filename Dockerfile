FROM python:3

ADD pswrdgen.py /

ENTRYPOINT [ "python", "./pswrdgen.py" ]
