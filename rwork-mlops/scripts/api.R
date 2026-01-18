library(plumber)
library(jsonlite)

source("monitor.R")

kmeans_model <- readRDS("../outputs/kmeans_artifact.rds")

#* Health check
#* @get /health
function() {
  list(status = "API running")
}
