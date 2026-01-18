library(readr)

data <- read_csv(
  "data/processed/cleaned_online_retail.csv",
  show_col_types = FALSE
)

features <- data[, -1]

scaled_data <- scale(features)

scaling_params <- list(
  center = attr(scaled_data, "scaled:center"),
  scale  = attr(scaled_data, "scaled:scale")
)

set.seed(42)  # any fixed number is fine

k <- 4  # chosen based on silhouette analysis

kmeans_model <- kmeans(
  scaled_data,
  centers = k,
  nstart = 50,
  iter.max = 100
)

data$Cluster <- kmeans_model$cluster

if (!dir.exists("outputs")) {
  dir.create("outputs", recursive = TRUE)
}

write_csv(data, "outputs/model_output.csv")

kmeans_artifact <- list(
  centers = kmeans_model$centers,
  scaling = scaling_params,
  k = k
)

saveRDS(kmeans_artifact, "outputs/kmeans_artifact.rds")
