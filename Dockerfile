FROM public.ecr.aws/lambda/python:3.8
COPY nyc_large.db .
COPY lambda.py .
CMD [ "lambda.handler" ]
