library(dplyr)
library(readxl)
library(readr)

data <- read_excel("data/raw/Online Retail.xlsx")

customer_features <- data %>%
  filter(
    !is.na(CustomerID),
    Quantity > 0,
    UnitPrice > 0
  ) %>%
  mutate(
    TotalPrice = Quantity * UnitPrice
  ) %>%
  group_by(CustomerID) %>%
  summarise(
    TotalSpend = sum(TotalPrice),
    TotalQuantity = sum(Quantity),
    Frequency = n_distinct(InvoiceNo),
    LastPurchaseDate = max(InvoiceDate),
    .groups = "drop"
  )

# Compute Recency (days since last purchase)
snapshot_date <- max(customer_features$LastPurchaseDate) + 1

customer_features <- customer_features %>%
  mutate(
    Recency = as.numeric(snapshot_date - LastPurchaseDate),
    TotalSpend = log1p(TotalSpend)  # reduce outlier impact
  ) %>%
  select(-LastPurchaseDate)

if (!dir.exists("data/processed")) {
  dir.create("data/processed", recursive = TRUE)
}

write_csv(
  customer_features,
  "data/processed/cleaned_online_retail.csv"
)
