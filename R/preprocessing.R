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
  mutate(TotalPrice = Quantity * UnitPrice) %>%
  group_by(CustomerID) %>%
  summarise(
    TotalSpend = sum(TotalPrice),
    TotalQuantity = sum(Quantity),
    Frequency = n()
  )

write_csv(customer_features, "data/processed/cleaned_online_retail.csv")

