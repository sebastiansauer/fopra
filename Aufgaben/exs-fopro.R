# ex fopro


# Setup -------------------------------------------------------------------




library(dplyr)

library(exams)
library(teachertools)
#options(digits = 2)


#Sys.setenv(R_CONFIG_ACTIVE = "dev")  # for testing
Sys.setenv(R_CONFIG_ACTIVE = "default")  # for production
#config <- config::get()
#config

# Maschine 1 (Macbook)
ex_dir <- "/Users/sebastiansaueruser/github-repos/rexams-exercises/exercises"

path_datenwerk <- "/Users/sebastiansaueruser/github-repos/datenwerk/posts"




# div ---------------------------------------------------------------------


exs <-
  c("nasa04.Rmd",
    "nasa05.Rmd",
    "anim01.Rmd",
    "anim02.Rmd",   
    "anim03.Rmd"
    )


exs_div <-
  c("diamonds-tidymodels01.Rmd",
    "tidymodels-penguins07.Rmd",
    "nasa04.Rmd")


# Datenwerk:
teachertools::render_exs(exs,
                         my_edir = ex_dir,
                         output_path = path_datenwerk,
                         render_html = FALSE,
                         render_moodle = FALSE,
                         render_pdf_print = FALSE,
                         render_markdown = FALSE,
                         render_yamlrmd = TRUE,
                         thema_nr = "1")

