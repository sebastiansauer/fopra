library(DiagrammeR)

m1 <-
  mermaid("
flowchart LR
  ff(Forschungsfrage)
  lit(Literaturrecherche)
  plan(Versuchsplanung)
  do(Durchführung)
  stat(Datenanalyse)
  interpret(Interpretation)

  ff --> lit
  lit --> plan
  plan --> do
  do --> stat
  stat --> interpret
  interpret --> ff
          ")


m1
