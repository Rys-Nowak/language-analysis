# Prównanie języka czeskiego do języka manuskryptu Wojnicza

## Prawo Zipfa
Gdy na podstawie ich korpusów językowych ustali się wykaz wyrazów ułożonych w malejącym porządku częstotliwości ich występowania, to ranga (numer porządkowy) wyrazu jest odwrotnie proporcjonalna do częstotliwości, zatem iloczyn częstotliwości i rangi powinien być wielkością stałą.

### Wyniki analizy dla najczęściej występujących 300 wyrazów

#### Częstotliwość występowania słów o kolejnych rangach - wykres powinien być hiperboliczny

<img src="out/czech/zipf_300.jpg">

Język czeski
<hr>

<img src="out/voynich/zipf_300.jpg">

Język z manuskryptu

#### Iloczyn częstotliwość występowania słów do ich rangi - wykres powinien być zbliżony do funkcji stałej

<img src="out/czech/zipf_coef_300.jpg">

Język czeski
<hr>

<img src="out/voynich/zipf_coef_300.jpg">

Język z manuskryptu

### Wniosek
Wykresy wskazują że dla słów o rangach 50-300, prawo Zipfa dla obu języków jest dobrze spełnione - odchylenia od stałej wartości są niewielkie. W przypadku języka z manuskryptu Wojnicza, z pominięciem kilku najczęściej występujących słów, są one zauważalnie mniejsze niż w analizowanym czeskim tekście. Wartości błędów średniokwadratowych dla dopasowanej przy użyciu np.polyfit stałej są zbliżone

## Analiza n-gramów
Analizę n-gramów zaczyna się od zliczania wystąpień sekwencji o ustalonej długości n w istniejących zasobach językowych. Zlicza się wszystkie pojedyncze wystąpienia (1-gramy, unigramy), dwójki (2-gramy, bigramy) i trójki (3-gramy, trigramy).
#### Dla języka czeskiego 10 najcześciej występujących bigramów wygląda następująco:
```
                   words  occurrences
              (jako, by)           29
               (a, jeho)           26
                (je, to)           24
                (by, se)           19
      (francesco, pazzi)           13
                  (a, v)           12
        (de, montesecco)           12
  (arcibiskup, salviati)           10
                (a, pak)           10
        (jeho, svatosti)           10
```
#### Dla Manuskryptu Wojnicza 10 najcześciej występujących bigramów wygląda następująco:
```
          words  occurrences
     (TOE, 8AM)           37
       (OR, AM)           32
  (SC8G, 4ODAM)           27
     (8AM, 8AM)           23
   (SCG, 4ODAM)           23
     (TOE, TOE)           22
    (4OE, TC8G)           22
  (TC8G, 4ODAM)           21
     (OE, SC8G)           21
     (8AM, TCG)           20
```
#### Język czeski 10 najcześciej występujących trigramów:
```
                         words  occurrences
                (jako, by, se)           10
               (s, maria, del)            7
           (maria, del, fiore)            7
      (okna, paláce, signorie)            4
               (jako, by, byl)            4
  (okna, florentské, signorie)            4
            (chrámu, s, maria)            4
                 (zdá, se, že)            4
   (v, člověčenství, kristovo)            4
            (můj, drahý, pier)            3
```
#### Manuskrypt Wojnicza 10 najcześciej występujących trigramów:
```
                     words  occurrences
        (OE, SC8G, 4ODC8G)            4
          (TCG, 4OE, TC8G)            4
            (8AM, 8G, 8AM)            3
  (4ODC8G, 4ODC8G, 4ODC8G)            3
        (SCG, 4ODAM, TC8G)            3
        (4OE, TC8G, 4ODAM)            3
        (SC8G, 4ODAM, SCG)            3
   (SC8G, 4ODC8G, 4ODCC8G)            3
     (SCC8G, 4ODC8G, TC8G)            3
        (OE, SC8G, 4ODCCG)            3
```
