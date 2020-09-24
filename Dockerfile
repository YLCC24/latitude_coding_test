FROM python:3.7
ARG export_file=some.json
COPY $export_file spec.json
COPY parser.py /
CMD ["python", "./parser.py"]
