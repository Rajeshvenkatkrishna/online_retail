library(cluster)
library(readr)

data <- read_csv(
  "data/processed/cleaned_online_retail.csv",
  show_col_types = FALSE
)

scaled_data <- scale(data[, -1])

km <- kmeans(
  scaled_data,
  centers = 4,
  nstart = 50,
  iter.max = 100
)

sil <- silhouette(km$cluster, dist(scaled_data))
avg_silhouette <- mean(sil[, 3])

if (!dir.exists("outputs")) {
  dir.create("outputs", recursive = TRUE)
}

writeLines(
  paste("Average Silhouette Score:", avg_silhouette),
  "outputs/metrics.txt"
)
