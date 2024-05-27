# Use Python 3.10 slim image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the files needed for installing dependencies to avoid cache invalidation
COPY pyproject.toml poetry.lock README.md ./

# Install Poetry
RUN pip install poetry

# Copy the rest of your application code
COPY streamlit_app ./streamlit_app
COPY tests ./tests

# Install dependencies using Poetry
# --no-dev: Avoid installing development dependencies
# --no-interaction: Do not ask any interactive question
# --no-root: Do not install the current project (useful when it's already included in pyproject.toml)
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-root

# Install the local package using Poetry
#RUN poetry install --no-dev
#COPY app.py data_loader.py plots.py ./
# Expose the port Streamlit will run on
EXPOSE 5002

# Use CMD to run your Streamlit app
# Adjust "app.py" if your Streamlit script is named differently
CMD ["streamlit", "run", "streamlit_app/app.py", "--server.port=5002"]
