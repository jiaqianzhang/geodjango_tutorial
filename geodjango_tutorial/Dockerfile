# Use a Miniconda base image
FROM continuumio/miniconda3

# Set environment variables for Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=geodjango_tutorial.settings

# Set the working directory
WORKDIR /app

# Install system dependencies, including libpoppler-dev and netcat
RUN apt-get update && apt-get install -y libpoppler-dev netcat-openbsd

# Copy environment YAML file and create the Conda environment
COPY ENV.yml .
RUN conda env create -f ENV.yml

# Activate the environment and set the PATH
ENV PATH=/opt/conda/envs/awm_env/bin:$PATH

# Expose the Django port
EXPOSE 8001

# Copy the Django project files into the container
COPY . .

# Command to run the Django development server
CMD ["conda", "run", "-n", "awm_env", "python", "manage.py", "runserver", "0.0.0.0:8001"]
