library(readr)


data <- read_csv("data/processed/cleaned_online_retail.csv")


features <- data[, -1]


scaled_data <- scale(features)


scaling_params <- list(
  center = attr(scaled_data, "scaled:center"),
  scale  = attr(scaled_data, "scaled:scale")
)

set.seed(123)

kmeans_model <- kmeans(
  scaled_data,
  centers = 4,
  nstart = 25
)


data$Cluster <- kmeans_model$cluster
write_csv(data, "outputs/model_output.csv")


kmeans_artifact <- list(
  centers = kmeans_model$centers,
  scaling = scaling_params,
  k = 4
)

saveRDS(kmeans_artifact, "outputs/kmeans_artifact.rds")


