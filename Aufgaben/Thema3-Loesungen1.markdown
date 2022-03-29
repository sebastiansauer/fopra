1.  **Aufgabe**\

    Berechnen Sie ein *95%-Perzintilintervall* für den *Anteil* der
    Autos mit *Automatik*-Getriebe!

    Diese Frage zielt ab auf die Ungewissheit der Beschreibung einer
    Variable (Automatikgetriebe) in der Population.

    Hinweis:

    -   Nutzen Sie Methoden der Bayes-Statistik.
    -   Vergessen Sie nicht, die nötigen R-Pakete zu starten.

    \
    **Lösung**

    ``` text
    data(mtcars)
    ```

    Explorative Analyse:

    ``` text
    mtcars %>% 
      count(am) %>% 
      mutate(prop = n/sum(n))
    ```

        ##   am  n    prop
        ## 1  0 19 0.59375
        ## 2  1 13 0.40625

    ``` text
    mtcars <-
      mtcars %>% 
      mutate(is_automatic = ifelse(am == 0, 1, 0))
    ```

    `stan_glm()` berechnet die Wahrscheinlichkeit für das Ereignis, das
    mit `1` verknüpft ist. Bei `am` ist das "manuelle Schaltung". Daher
    haben wir noch eine andere Variable angelegt, `is_automatic`, die
    als `1` "Automatik-Getriebe" hat.

    ``` text
    m1 <- stan_glm(is_automatic ~ 1,
                   family = binomial("logit"),
                   refresh = 0,
                   data = mtcars)

    coef(m1) %>% invlogit()
    ```

        ## (Intercept) 
        ##   0.5952863

    ``` text
    posterior_interval(m1, prob = .95) %>% invlogit()
    ```

        ##                 2.5%     97.5%
        ## (Intercept) 0.429943 0.7580393
