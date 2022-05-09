1.  **Aufgabe**\

    In einer Studie untersuchte Frau Prof. Dr. Klug Ursachen von
    Entscheidungen im Rahmen von Einstellungen und Verhalten bei Pop-up
    Stores.

    U.a. wurden folgende Fragen untersucht:

    -   Welchen (kausalen) Effekt hat die Distanz zum und Lage des
        Pop-up-Stores hinsichtlich der AV?
    -   Wie stark ist der Moderatoreffekt von Variablen wie z.B.
        Innovationsorientierung, Shopping-Relevnaz und Soziodemografika?
    -   Ist ein Effekt auf Einstellung, Verhaltensintention und
        Verhalten zu beobachten?

    Es handelt sich um ein experimentelles Design mit zwei Faktoren
    (Lage und Distanz) mit jeweils 3 Stufen.

    Ein Teil der Daten ist (nur) für Lehrzwecke freigeben.

    Folgende Materialien stehen bereit:

    -   [Roh-Datensatz](https://raw.githubusercontent.com/sebastiansauer/Lehre/main/data/popupstore/data/d1a.csv),
        $n = 90$, Gruppen 1-3
    -   [Studienkonzept](https://github.com/sebastiansauer/Lehre/blob/main/data/popupstore/materials/0_Konzept_Pop-up_Location_2018-10-30.pdf)
    -   [Frageobgen](https://github.com/sebastiansauer/Lehre/blob/main/data/popupstore/materials/A_FB_Pop-up_Location_neu_mitKonstrukten.pdf)
    -   [Codebook](https://github.com/sebastiansauer/Lehre/blob/main/data/popupstore/docs/codebook.xlsx)

    # Aufgaben

    1.  Entfernen Sie leere Zeilen und Spalten aus dem Datensatz. Tipp:
        Nutzen Sie das R-Paket `{{janitor}}`.
    2.  Entfernen Sie konstante Variablen. Tipp: Nutzen Sie das R-Paket
        `{{janitor}}`.
    3.  Prüfen Sie auf Duplikate, d.h. doppelte Zeilen. Tipp: Nutzen Sie
        das R-Paket `{{janitor}}`.
    4.  Entfernen Sie alle Spalten, die Zeit-Objekte enthalten.
    5.  Ersetzen Sie leere Zellen sowie Zellen mit Inhalt `"N/A"` durch
        `NA`, also durch einen fehlenden Wert. Tipp: `na_if()` aus
        `{{dplyr}}`.
    6.  Rekodieren Sie die Anker (Labels) der Ratingskala in Zahlen und
        zwar von -3 bis +3! Tipp: Nutzen Sie `recode()` aus `{{dplyr}}`.
    7.  Berechnen Sie Spalten-Mittelwerte für alle Konstrukte, die die
        Ratingskala verwenden. Tipp: Nutzen Sie `rowwise()` und
        `c_across()`.

    \
    **Lösung**

    Ad 1.

    Daten laden:

    ``` text
    d_url <- "https://raw.githubusercontent.com/sebastiansauer/Lehre/main/data/popupstore/data/d1a.csv"

    d1a <- read_csv(d_url)
    ```

        ## Rows: 90 Columns: 196
        ## ── Column specification ──────────────────────────
        ## Delimiter: ","
        ## chr   (76): v004, v008, v009, v010, v011, v012...
        ## dbl    (5): v001, v003, v005, v023, v109
        ## lgl  (112): v024, v025, v026, v027, v028, v029...
        ## dttm   (3): v002, v006, v007
        ## 
        ## ℹ Use `spec()` to retrieve the full column specification for this data.
        ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

    ``` text
    dim(d1a)
    ```

        ## [1]  90 196

    Die Tabelel umfasst 90 Zeilen und 196 Spalten.

    Leere Zeilen/Spalten entfernen:

    ``` text
    library(janitor)
    d2 <-
      d1a %>% 
      remove_empty()
    ```

        ## value for "which" not specified, defaulting to c("rows", "cols")

    Ad 2.

    ``` text
    library(janitor)
    d3 <-
      d2 %>% 
      remove_constant()
    ```

    Ad 3.

    ``` text
    d3 %>% 
      get_dupes()
    ```

        ## No variable names specified - using all columns.

        ## No duplicate combinations found of: v001, v002, v003, v005, v006, v007, v008, v009, v010, ... and 74 other variables

        ## # A tibble: 0 × 84
        ## # … with 84 variables: v001 <dbl>, v002 <dttm>,
        ## #   v003 <dbl>, v005 <dbl>, v006 <dttm>,
        ## #   v007 <dttm>, v008 <chr>, v009 <chr>,
        ## #   v010 <chr>, v011 <chr>, v012 <chr>,
        ## #   v013 <chr>, v014 <chr>, v015 <chr>,
        ## #   v016 <chr>, v017 <chr>, v018 <chr>,
        ## #   v019 <chr>, v020 <chr>, v021 <chr>, …

    Keine Duplikate zu finden.

    Ad 4.

    ``` text
    d4 <-
      d3 %>% 
      select(-c(v002, v006, v007))
    ```

    Ad 5.

    ``` text
    d4 %>% 
      mutate(v001 = na_if(v001, ""),
             v001 = na_if(v001, "N/A"))
    ```

        ## # A tibble: 90 × 80
        ##     v001  v003       v005 v008   v009  v010  v011 
        ##    <dbl> <dbl>      <dbl> <chr>  <chr> <chr> <chr>
        ##  1   794    25 1031050258 2a02:… <NA>  Ja    Ja   
        ##  2   146    25 1376736840 2a02:… <NA>  Ja    Ja   
        ##  3   459     4  355469450 2003:… http… Nein  Ja   
        ##  4   324    25  995386148 134.2… http… Ja    Ja   
        ##  5   257    25  689485052 2003:… http… Nein  Nein 
        ##  6   182    25 1702405999 2003:… http… Nein  Nein 
        ##  7    95    25 1699812941 93.13… http… Ja    Nein 
        ##  8   355    25 1599676009 2a02:… http… Ja    Nein 
        ##  9   570    25  809829273 2003:… http… Nein  Nein 
        ## 10   173    25   76734057 134.2… http… Ja    Nein 
        ## # … with 80 more rows, and 73 more variables:
        ## #   v012 <chr>, v013 <chr>, v014 <chr>,
        ## #   v015 <chr>, v016 <chr>, v017 <chr>,
        ## #   v018 <chr>, v019 <chr>, v020 <chr>,
        ## #   v021 <chr>, v022 <chr>, v023 <dbl>,
        ## #   v033 <chr>, v034 <chr>, v035 <chr>,
        ## #   v036 <chr>, v037 <chr>, v038 <chr>, …

    Und so weiter für alle Spalten ...

    Puh, geht das nicht schlauer?

    Ja, geht. Hier ein kleiner Trick:

    ``` text
    d5 <-
      d4 %>% 
      map_df(na_if, "") %>% 
      map_df(na_if, "N/A")
    ```

    Mit `map_df()` kann man eine Funktion, hier `na_if()` auf jede
    Spalte der Tabelle (hier: `d5`) anwenden. Als Ergebnis dieses
    "Funktions-Mapping" soll wieder eine Tabelle - daher `map_df`
    zurückgegeben werden.

    Mal ein Check: Die Anzahl der fehlenden Werte müsste sich jetzt
    erhöht haben im Vergleich zur letzten Version des Datensatz, `d4`:

    ``` text
    sum(is.na(d4))
    ```

        ## [1] 1806

    ``` text
    sum(is.na(d5))
    ```

        ## [1] 1893

    Hm, gar nicht so viele mehr. Aber grundsätzlich hat es funktioniert
    :-)

    Sie brauchen `map_df()` nicht zu verwenden. Es geht auch ohne. Mit
    `map_df()` ist es nur komfortabler.

    Ad 6.

    Die Item-Positionen, wann also die Items der Ratingskala beginnen
    und wann (an welcher Spaltenposition) sie enden, ist im Fragebogen
    ersichtlich.

    ``` text
    d5 %>% 
      mutate(v033_r = recode(v033,
          "lehne voll und ganz ab" = -3,
          "lehne ab" = -2,
          "lehne eher ab" = -1,
          "weder/noch" = 0,
          "stimme eher zu" = 1,
          "stimme zu" = 2,
          "stimme voll und ganz zu" = 3,
          .default = NA_real_  # Ansonsten als NA und zwar NA vom Typ "reelle Zahl"
      )) %>% 
      select(v001, v033, v033_r) %>% 
      head(10)
    ```

        ## # A tibble: 10 × 3
        ##     v001 v033                    v033_r
        ##    <dbl> <chr>                    <dbl>
        ##  1   794 stimme voll und ganz zu      3
        ##  2   146 stimme eher zu               1
        ##  3   459 <NA>                        NA
        ##  4   324 stimme eher zu               1
        ##  5   257 lehne eher ab               -1
        ##  6   182 stimme zu                    2
        ##  7    95 stimme eher zu               1
        ##  8   355 stimme zu                    2
        ##  9   570 stimme eher zu               1
        ## 10   173 lehne eher ab               -1

    Das hat also funktioniert. Aber das jetzt für alle Spalte zu
    übernehmen, puh, viel zu langweilig. Gibt's da vielleicht einen
    Trick?

    Ja, gibt es.

    ``` text
    d6 <-
      d5 %>%
      mutate(across(
        .cols = c(v033:v056, v087:v104),
        .fns = ~ recode(.,
          "lehne voll und ganz ab" = -3,
          "lehne ab" = -2,
          "lehne eher ab" = -1,
          "weder/noch" = 0,
          "stimme eher zu" = 1,
          "stimme zu" = 2,
          "stimme voll und ganz zu" = 3,
          .default = NA_real_  # Andere Wete als NA (Fehlende Werte) vom Typ "reelle Zahl" kennzeichnen
        )
      ))
    ```

    Mit `across()` kann man eine Funktion (oder mehrere), `.fns`, über
    mehrere Spalten, `.cols` anwenden, hier wenden wir `recode()` auf
    alle Spalten der Ratingskala an.

    Ad 7.

    ``` text
    d7 <-
      d6 %>%
      rowwise() %>%  # Zeilenweise arbeiten im Folgenden
      mutate(
        exp_avg = mean(c_across(v033:v039), na.rm = TRUE),
        neu_avg = mean(c_across(v040:v042), na.rm = TRUE),
        att_avg = mean(c_across(v043:v047), na.rm = TRUE),
        ka_avg = mean(c_across(v048:v053), na.rm = TRUE), 
        wom_avg = mean(c_across(v054:v056), na.rm = TRUE),
        innp_avg = mean(c_across(v087:v092), na.rm = TRUE),
        imp_avg = mean(c_across(v093:v096), na.rm = TRUE),
        hedo_avg = mean(c_across(v097:v100), na.rm = TRUE),
        sho1_avg = mean(c_across(v101:v104), na.rm = TRUE)
      ) %>%
      relocate(ends_with("_avg"), .after = v008)  # wir verschieben alle Spalten, die mit `_avg` enden nach vorne
    ```

    `c_across()` ist wie `c()`. Allerdings funktioniert `c()` leider
    *nicht* für zeilenweise Operationen. Daher braucht es einen Freund,
    der das kann, `c_across()`.
