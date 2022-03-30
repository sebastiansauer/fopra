course_dates_file <- "Interna/course-dates.yaml"
content_file <- "Interna/modul-zsfg.yaml"

header_level <- 3


master_table <-
  build_master_course_table2(course_dates_file,
                             content_file)



name <- "Coaching"
id <- 3
master_table[[name]][id]



out <- master_table[[name]][[3]]
out

if (!is.null(out)){
  cat(paste0(str_c(rep("#", header_level + 1), collapse = "")," ", name, " \n"))
  cat("\n")
  for (i in out) {
    cat(paste0("- ", i))
    cat("\n")
  }

  cat("\n")
  cat("\n")

}
