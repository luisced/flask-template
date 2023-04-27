# 1. Install python image
FROM python:3.11.3-slim-bullseye
# 2. Set the working directory
WORKDIR /genericApp
# 3. Copy the dependencies file to the working directory
COPY . .
# 2. Give user permissions to modify all contents
RUN chmod +x sql 
# 4. Install dependencies
ENV FLASK_ENV development
# 5. Set environment to Debug mode in order to enable hotreload
ENV DEBUG true
# 6. Set the timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 7. Install dependencies
RUN pip install --upgrade pip && pip3 install -r requirements.txt
# 8. Run the container
CMD ["python", "App/run.py"]
# 9. Expose the application
EXPOSE 5555
