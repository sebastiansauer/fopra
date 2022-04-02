# Thema 04

library(nomnoml)

p1 <-
"
#direction: right
[Treatment]->[Ergebnis]
[Anderes T]->[Anderes E]
"

nomnoml(p1)
nomnoml(p1,png = "chunk-img/Thema04/p1.png")


p2 <-
"
[Ursache U] -> [Effekt]
[Versuchosobjekte O]->[Effekt]
[Zeit Z]->[Effekt]
[Rahmen R]->[Effekt]
[Messinstrument M]->[Effekt]
"

nomnoml(p2)
nomnoml(p2,png = "chunk-img/Thema04/p2.png")
