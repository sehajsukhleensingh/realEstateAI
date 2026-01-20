# BASE IMAGE
FROM python:3.13.7-slim 

# Working Directory 
WORKDIR /app

# copying the dependencies 
COPY requirements.txt . 

# installing dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# copy all project files 
COPY . .

# expose the streamlit port 
EXPOSE 8501 

# final command to run app 

CMD ["streamlit","run","website/main.py"]


