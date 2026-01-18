log_event <- function(message) {
  cat(
    paste(Sys.time(), "-", message, "\n"),
    file = "logs/app.log",
    append = TRUE
  )
}
