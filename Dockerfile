FROM public.ecr.aws/lambda/python:3.9.2022.01.10.10-x86_64

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY nyc_medium.db .
# Copy function code
COPY lambda.py ${LAMBDA_TASK_ROOT}
RUN chmod -R 755 ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda.handler" ]