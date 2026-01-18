FROM rstudio/plumber:latest

# REMOVE the default ENTRYPOINT from rstudio/plumber
ENTRYPOINT []

WORKDIR /app

# Explicitly install ALL packages used in api.R
RUN R -e "install.packages(c('plumber','jsonlite','here'), repos='https://cloud.r-project.org')"

# Copy project files
COPY scripts/ scripts/
COPY outputs/ outputs/
COPY logs/ logs/

EXPOSE 8000

# Start the API explicitly
CMD ["R", "-e", "library(plumber); library(jsonlite); library(here); pr <- plumber::plumb('scripts/api.R'); pr$run(host='0.0.0.0', port=8000)"]
