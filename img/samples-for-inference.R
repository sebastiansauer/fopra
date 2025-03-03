library(tidyverse)
library(see)
library(patchwork)

theme_set(theme_minimal())


n_samples <- 1e3
sample_size <- 30
set.seed(42)

d <-
  tibble(height = rnorm(n = n_samples*sample_size,
                        mean = 172.5,
                        sd = 7),
         group = rep(x = 1:n_samples, each = sample_size))


group_means <- d %>%
  group_by(group) %>%
  summarise(mean_height = mean(height))

# Merge the group means back to the original dataframe
d <- d %>%
  left_join(group_means, by = "group")



p_samples <-
  d |>
  filter(group < 11) |>
  mutate(group = group) |>
  ggplot() +
  aes(x = height, y = group, group = group) +
  geom_violin() +
  geom_point(position = position_jitter(height = 0.2, width = .1), alpha = 0.5) +
  geom_point(aes(x = mean(group_means$mean_height), y = group), color = okabeito_colors("orange"), size = 3) +
  theme(
    strip.background = element_blank(),
    strip.text = element_text(size = 8),
    axis.text.y = element_blank(),
    axis.ticks.y = element_blank()
  ) +
  labs(
    x = "Körpergröße",
    y = "Stichprobe",
    title = "Stichproben Körpergröße",
    caption = paste0("Umfang jeder Stichprobe: ", sample_size)
  )


#p_samples



# Display the plot
#print(p_samples)

# source: https://www.destatis.de/EN/Themes/Society-Environment/Health/Health-Status-Behaviour-Relevant-Health/Tables/liste-height-weight-body-mass-index-population-sex-age-groups.html#51240



p_etc <- ggplot() +
  xlim(0, 1) +
  ylim(0, 1) +
  theme_void() +  # Remove all background and axes
  geom_text(aes(x = 0.5, y = 0.5, label = "etc."), size = 10)


#p_etc

p_arrow <- ggplot() +
  xlim(0, 2) +
  ylim(0, 1) +
  theme_void() +  # Remove all background and axes
  geom_segment(aes(x = 0.5, y = 0.5, xend = 1.5, yend = 0.5),
               arrow = arrow(length = unit(0.2, "inches"), type = "closed"))
#p_arrow

#
# group_means |>
#   ggplot(aes(x = mean_height)) +
#   geom_density() +
#   geom_rug() +
#   geom_vline(xintercept = mean(group_means$mean_height))

population_mean <- 172.5
sample_mean <- round(mean(group_means$mean_height), 2)
sample_sd <- round(sd(group_means$mean_height), 2)

# Create the density plot with additional elements
p_all_samples <- group_means |>
  ggplot(aes(x = mean_height)) +
  geom_histogram(fill = "grey40", alpha = 0.3) +
  geom_rug() +
  geom_vline(xintercept = 172.5, linetype = "dashed", color = okabeito_colors("orange")) +
  geom_vline(xintercept = sample_mean, linetype = "dotted", color = okabeito_colors("green")) +
  geom_errorbarh(aes(y = -0.03,
                     xmin = sample_mean - sample_sd,
                     xmax = sample_mean + sample_sd),
                  color = okabeito_colors("purple"),
                 size = 2) +
  annotate("text", x = 172.5, y = Inf, label = "mu = 172.5",
           color = okabeito_colors("orange"), angle = 90, vjust = -0.5, hjust = 1) +
  annotate("text", x = sample_mean, y = 0,
           label = paste("MW der MW = ", round(sample_mean, 2)),
           color = okabeito_colors("green"), angle = 90, vjust = 1, hjust = -1) +
  annotate("text", x = 172.5, y = 0, label = paste0("sd = ",sample_sd),
           color = okabeito_colors("purple"), vjust = 0) +
  labs(
    title = "Verteilung der Mittelwerte",
    x = "Mittlere Größe",
    y = "",
    caption = "Quelle: DEStatis"
  ) +
  theme_minimal() +
  theme(
    axis.text.y = element_blank(),  # Remove y-axis text
    axis.ticks.y = element_blank(), # Remove y-axis ticks
    axis.title.y = element_blank()  # Remove y-axis title
  )


# Display the plot
#print(p_all)


layout <- "AAABCDDD"

p_infence_with_samples <- p_samples + p_etc + p_arrow + p_all_samples + plot_layout(design = layout)
#p_infence_with_samples

