# ===============================
# Load required libraries
# ===============================
.libPaths(c("~/R/library", .libPaths()))

required_packages <- c("dplyr", "readr", "readxl")

for (pkg in required_packages) {
  if (!require(pkg, character.only = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org", lib = "~/R/library")
    library(pkg, character.only = TRUE)
  }
}

# ===============================
# Load raw data
# ===============================
data <- read_excel("data/raw/Online Retail.xlsx")

# ===============================
# Create customer-level features
# ===============================
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

# ===============================
# Compute Recency
# ===============================
snapshot_date <- max(customer_features$LastPurchaseDate) + 1

customer_features <- customer_features %>%
  mutate(
    Recency = as.numeric(snapshot_date - LastPurchaseDate),
    TotalSpend = log1p(TotalSpend)  # reduce effect of extreme spenders
  ) %>%
  select(-LastPurchaseDate)

# ===============================
# Compute RFM Scores
# ===============================
customer_features <- customer_features %>%
  mutate(
    M_Score = case_when(
      TotalSpend <= quantile(TotalSpend, 0.33) ~ 1,
      TotalSpend <= quantile(TotalSpend, 0.66) ~ 2,
      TRUE ~ 3
    ),
    F_Score = case_when(
      Frequency <= quantile(Frequency, 0.33) ~ 1,
      Frequency <= quantile(Frequency, 0.66) ~ 2,
      TRUE ~ 3
    ),
    R_Score = case_when(
      Recency <= quantile(Recency, 0.33) ~ 3,
      Recency <= quantile(Recency, 0.66) ~ 2,
      TRUE ~ 1
    )
  )

# ===============================
# Create Customer Labels
# ===============================
customer_features <- customer_features %>%
  mutate(
    RFM_Score = R_Score + F_Score + M_Score,
    Customer_Label = case_when(
      RFM_Score >= 7 ~ "High",
      RFM_Score >= 4 ~ "Medium",
      TRUE ~ "Low"
    )
  )

# ===============================
# Save processed data
# ===============================
if (!dir.exists("data/processed")) {
  dir.create("data/processed", recursive = TRUE)
}

write_csv(
  customer_features,
  "data/processed/cleaned_online_retail.csv"
)

cat("Customer preprocessing and labeling completed successfully\n")
