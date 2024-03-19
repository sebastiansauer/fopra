library(tidyverse)

out <-

get_pckgs <- function(pattern = "\\.qmd$|\\.R$",
                      recursive = TRUE) {

list.files(pattern = pattern, recursive = recursive) %>%
  purrr::map(readLines) %>%
  stringr::str_extract_all("library\\(([^)]+)\\)|require\\(([^)]+)\\)") %>%
  unlist() %>%
  unique() %>%
  sort()
}

