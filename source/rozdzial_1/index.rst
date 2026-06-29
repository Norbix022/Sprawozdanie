=====
Wstęp
=====

:Autor: Norbert Antonovitch

Wprowadzenie do sprawozdania
============================

Niniejsze sprawozdanie stanowi podsumowanie zajęć laboratoryjnych, podczas których zrealizowano pełen cykl projektowy relacyjnej bazy danych dla sklepu internetowego. Prace rozpoczęto od przygotowania kompleksowej dokumentacji projektowej, analizy procesów biznesowych oraz stworzenia prototypów struktur w formacie JSON. Następnie opracowano modele konceptualne i logiczne, wykorzystując do tego celu diagramy Chena oraz notację IE. 

Ostatnim etapem projektu była fizyczna implementacja zaprojektowanych modeli w systemach bazodanowych PostgreSQL oraz SQLite. Środowiska te zostały następnie zasilone wygenerowanymi danymi testowymi, a poprawność struktury zweryfikowano za pomocą zestawu zaawansowanych zapytań SQL.

Wnioski z przeprowadzonych ćwiczeń
==================================

Na podstawie przeprowadzonych zajęć laboratoryjnych i eksperymentów z modelami fizycznymi można sformułować następujące wnioski końcowe:

* **Fundament projektowy:** Rzetelnie przygotowana dokumentacja oraz prawidłowo wykonana normalizacja bazy danych stanowią niezbędną podstawę do bezbłędnego i sprawnego wdrożenia modelu fizycznego.
* **Przewaga PostgreSQL:** Podczas implementacji i testowania zapytań wyraźnie zauważalna była dominacja systemu PostgreSQL w kontekście budowy profesjonalnych rozwiązań. Wynika ona z rygorystycznego typowania danych, bogatej składni SQL oraz natywnego wymuszania więzów integralności.
* **Ograniczenia SQLite:** Silnik SQLite, choć jest narzędziem wygodnym i szybkim do uruchomienia (jako baza plikowa), ma uproszczoną strukturę, przez co jest mniej przewidywalny i bezpieczny niż zaawansowane relacyjne systemy zarządzania bazami danych.
* **Złożone operacje:** Wykonywanie skomplikowanych zapytań, opartych na podzapytaniach i wielokrotnych złączeniach tabel (JOIN), udowodniło, że to PostgreSQL zapewnia wydajność, stabilność i precyzję niezbędną do profesjonalnej analityki danych.

Wykaz repozytoriów
==================

Główne repozytorium sprawozdania
--------------------------------
Poniżej znajduje się link do mojego repozytorium z kodem sprawozdania wygenerowanego przy użyciu kompilatora Sphinx:

* **Link:** https://github.com/Norbix022/Sprawozdanie

Repozytorium z modelami fizycznymi bazy
---------------------------------------
Odnośnik do repozytorium zawierającego kody źródłowe, modele fizyczne oraz skrypty inicjalizujące bazę danych:

* **Link:** https://github.com/Koko9077/Model-fizyczny-baz

Repozytoria reszty grupy (badania literaturowe)
-----------------------------------------------
Poniżej zestawiono odnośniki do publicznych repozytoriów prowadzonych przez resztę grupy, w których poruszono dodatkowe zagadnienia techniczne:

* **Grupa 1: Sprzęt dla bazy danych** https://github.com/karaskamil/Sprzet-dla-bazy-danych.git
* **Grupa 2: Konfiguracja bazy danych** https://github.com/Youarecheck/Bazy_Danych_Tematyczne_Repo_MK.git
* **Grupa 3: Kontrola i konserwacja** https://github.com/pawlos1337/Bazy-danych-temat.git
* **Grupa 4: Monitorowanie i diagnostyka** https://github.com/OskarProgrammer/monitorowanie_i_diagnostyka.git
* **Grupa 5: Wydajność, skalowanie i replikacja** https://github.com/KMachoK/Tematyczne.git
* **Grupa 6: Partycjonowanie danych** https://github.com/domino0472/Partycjonowani-Danych
* **Grupa 7: Bezpieczeństwo** https://github.com/oski486/BazyDanych-Subject.git
* **Grupa 8: Kopie zapasowe i odzyskiwanie danych** https://github.com/Koko9077/Kopie-zapasowe-i-odzyskiwanie-danych.git
