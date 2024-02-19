FROM ubuntu

#RUN apt update -y

#RUN apt install python3 -y

#RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt update -y && apt install -y python3 python3-pip

RUN mkdir /app1

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the tokenizer and model into the container
COPY DenseNet121.h5 .

COPY app.py /app1/

RUN chown -R 7860:7860 /app1
#RUN chown -R $(whoami):$(whoami) /app1

# Command to run the Gradio app when the container is launched
CMD ["python3", "/app1/app.py", "--host", "0.0.0.0", "--port", "7860"]