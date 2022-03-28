# Thema 3
# Populationsbeschreibende Studien



library(rstanarm)
library(tidyverse)
data(mtcars)

# Wie groß ist der Anteil der Autos mit 8 Zylindern?

mtcars <-
  mtcars %>%
  mutate(has_8_cyl = ifelse(cyl == 8, 1, 0))

m1 <- stan_glm(has_8_cyl ~ 1, data = mtcars,
               family = binomial(link = "logit"),
               refresh = 0)


coef(m1) %>% invlogit()

posterior_interval(m1, pars = "(Intercept)") %>% invlogit()

plot(m1)



# Was ist die mittlere PS-Zahl?


m2 <- stan_glm(hp ~ 1, data = mtcars,
               refresh = 0)

coef(m2)
posterior_interval(m2, pars = "(Intercept)")
