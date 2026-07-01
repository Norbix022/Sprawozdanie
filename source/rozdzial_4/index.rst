======================================================
Definiowanie bazy danych i wprowadzanie danych do bazy
======================================================

:Autorzy: Norbert Antonovitch, Michał Bednarczyk, Jan Balazs de Borbatviz

Definicja bazy danych w wariantach PostgreSQL i SQLite
------------------------------------------------------

W projekcie zastosowano dwa warianty definicji schematu bazy danych: dla PostgreSQL oraz dla SQLite. Oba warianty odwzorowują tę samą strukturę logiczną, jednak różnią się doborem typów danych i składnią definicji kluczy głównych oraz obcych.

W wariancie PostgreSQL przyjęto rygorystyczne typowanie danych. Identyfikatory zdefiniowano z użyciem typu ``SERIAL``, pola tekstowe opisano typem ``VARCHAR`` o ograniczonej długości, natomiast wartości finansowe zapisano w typie ``NUMERIC(10,2)``, zapewniającym odpowiednią precyzję obliczeń.

.. code-block:: sql

   -- Wariant PostgreSQL
   CREATE TABLE kategorie (
      id_kategorii SERIAL PRIMARY KEY,
      nazwa VARCHAR(100) NOT NULL
   );

   CREATE TABLE klienci (
      id_klienta SERIAL PRIMARY KEY,
      imie VARCHAR(50) NOT NULL,
      nazwisko VARCHAR(50) NOT NULL,
      email VARCHAR(255) UNIQUE NOT NULL,
      telefon VARCHAR(15),
      ulica VARCHAR(255),
      miasto VARCHAR(50),
      kod_pocztowy VARCHAR(15)
   );

   CREATE TABLE produkty (
      id_produktu SERIAL PRIMARY KEY,
      id_kategorii INTEGER NOT NULL,
      nazwa VARCHAR(255) NOT NULL,
      cena_bazowa NUMERIC(10,2) NOT NULL,
      CONSTRAINT fk_kategoria
         FOREIGN KEY (id_kategorii) REFERENCES kategorie(id_kategorii)
   );

   CREATE TABLE zamowienia (
      id_zamowienia SERIAL PRIMARY KEY,
      id_klienta INTEGER NOT NULL,
      data_zlozenia TIMESTAMP NOT NULL,
      status VARCHAR(50) NOT NULL,
      CONSTRAINT fk_klient
         FOREIGN KEY (id_klienta) REFERENCES klienci(id_klienta)
   );

   CREATE TABLE szczegoly_zamowienia (
      id_zamowienia INTEGER NOT NULL,
      id_produktu INTEGER NOT NULL,
      ilosc SMALLINT NOT NULL CHECK (ilosc > 0),
      cena_historyczna NUMERIC(10,2) NOT NULL,
      PRIMARY KEY (id_zamowienia, id_produktu),
      CONSTRAINT fk_zamowienie
         FOREIGN KEY (id_zamowienia) REFERENCES zamowienia(id_zamowienia),
      CONSTRAINT fk_produkt
         FOREIGN KEY (id_produktu) REFERENCES produkty(id_produktu)
   );

Wariant SQLite został dostosowany do prostszego modelu typów danych oferowanego przez ten silnik. Typ ``SERIAL`` zastąpiono konstrukcją ``INTEGER PRIMARY KEY AUTOINCREMENT``, pola tekstowe oraz daty zapisano jako ``TEXT``, natomiast wartości liczbowe o charakterze ciągłym opisano typem ``FLOAT``.

.. code-block:: sql

   -- Wariant SQLite
   CREATE TABLE kategorie (
      id_kategorii INTEGER PRIMARY KEY AUTOINCREMENT,
      nazwa TEXT NOT NULL
   );

   CREATE TABLE klienci (
      id_klienta INTEGER PRIMARY KEY AUTOINCREMENT,
      imie TEXT NOT NULL,
      nazwisko TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      telefon TEXT,
      ulica TEXT,
      miasto TEXT,
      kod_pocztowy TEXT
   );

   CREATE TABLE produkty (
      id_produktu INTEGER PRIMARY KEY AUTOINCREMENT,
      id_kategorii INTEGER NOT NULL,
      nazwa TEXT NOT NULL,
      cena_bazowa FLOAT NOT NULL,
      FOREIGN KEY (id_kategorii) REFERENCES kategorie(id_kategorii)
   );

   CREATE TABLE zamowienia (
      id_zamowienia INTEGER PRIMARY KEY AUTOINCREMENT,
      id_klienta INTEGER NOT NULL,
      data_zlozenia TEXT NOT NULL,
      status TEXT NOT NULL,
      FOREIGN KEY (id_klienta) REFERENCES klienci(id_klienta)
   );

   CREATE TABLE szczegoly_zamowienia (
      id_zamowienia INTEGER NOT NULL,
      id_produktu INTEGER NOT NULL,
      ilosc INTEGER NOT NULL CHECK (ilosc > 0),
      cena_historyczna FLOAT NOT NULL,
      PRIMARY KEY (id_zamowienia, id_produktu),
      FOREIGN KEY (id_zamowienia) REFERENCES zamowienia(id_zamowienia),
      FOREIGN KEY (id_produktu) REFERENCES produkty(id_produktu)
   );

Wybór mechanizmu wprowadzania danych
------------------------------------

W celu zainicjowania bazy danymi testowymi zdecydowano się na wykorzystanie klasycznych, pojedynczych instrukcji ``INSERT`` w języku SQL. Wybór tego bezpośredniego podejścia podyktowany był niewielkim rozmiarem przygotowanego zbioru danych, który służył jedynie do weryfikacji poprawności struktury logicznej i więzów integralności w środowiskach PostgreSQL oraz SQLite. Wykonanie zwykłych skryptów SQL pozwoliło na szybkie zasilenie tabel i natychmiastowe przetestowanie relacji.

Należy jednak wyraźnie zaznaczyć, że w docelowych aplikacjach produkcyjnych lub przy pracy z większymi wolumenami danych, ręczne przygotowywanie instrukcji ``INSERT`` jest skrajnie nieefektywne. W takich scenariuszach optymalną praktyką jest agregacja danych wejściowych w ustrukturyzowanych plikach, takich jak ``JSON`` lub ``CSV``. Pozwala to na pełną automatyzację za pomocą dedykowanych skryptów (np. w języku Python) oraz wykorzystanie mechanizmów wstawiania wsadowego, np. funkcji ``executemany()`` z biblioteki ``sqlite3`` czy narzędzi ORM pokroju ``SQLAlchemy``. Przesyłanie wielu rekordów w ramach jednego wywołania sieciowego drastycznie ogranicza narzut komunikacyjny, pozwala na lepsze zarządzanie transakcjami serwera bazy danych i znacząco poprawia ogólną wydajność.

Komentarz do procesu wprowadzania danych
----------------------------------------

Proces zasilania bazy danych musiał uwzględniać zależności wynikające z więzów integralności referencyjnej. Z tego względu kolejność wprowadzania danych za pomocą instrukcji ``INSERT`` nie mogła być przypadkowa i musiała ściśle odzwierciedlać strukturę relacyjną modelu. 

Kolejność wprowadzania danych była następująca:

1. W pierwszej kolejności zaimportowano dane do tabel niezależnych, czyli ``kategorie`` oraz ``klienci``.
2. Następnie zasilono tabelę ``produkty``. Operacja ta była możliwa dopiero po wcześniejszym utworzeniu kategorii, ponieważ każdy produkt musi być przypisany do istniejącej encji nadrzędnej.
3. W kolejnym kroku wprowadzono rekordy do tabeli ``zamowienia``, przypisując je do istniejących w bazie klientów.
4. Na końcu uzupełniono tabelę ``szczegoly_zamowienia``, która pełni funkcję encji asocjacyjnej i łączy identyfikatory zamówień oraz produktów. Wymaga to wcześniejszego istnienia obu powiązanych rekordów.

Takie uporządkowanie procesu importu danych wynika bezpośrednio z konstrukcji schematu relacyjnego i stanowi warunek poprawnego zachowania integralności bazy. W praktyce oznacza to, że dane nadrzędne muszą zostać zapisane przed danymi zależnymi.
