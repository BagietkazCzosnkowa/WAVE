# WAVE — Water Autonomous Vehicle Ecosystem

> **Autonomiczne jednostki nawodne do zbierania danych i realizacji misji badawczych.**

WAVE (*Water Autonomous Vehicle Ecosystem*) to projekt systemu autonomicznych jednostek nawodnych (**ASV — Autonomous Surface Vehicles**) wraz z oprogramowaniem do planowania, zarządzania i przetwarzania danych z misji.

Celem projektu jest stworzenie możliwie otwartego i modułowego systemu, który pozwala wykorzystać niewielkie, autonomiczne jednostki nawodne do wykonywania zadań, które normalnie wymagałyby ręcznego pomiaru lub wykorzystania znacznie droższego sprzętu.

Projekt jest obecnie rozwijany jako **Proof of Concept (POC)**.

---

## 🇵🇱 Polski

### Główna idea

WAVE łączy autonomiczne jednostki nawodne z systemem komputerowego zarządzania misją.

W podstawowej wersji jednostka ma:

* samodzielnie poruszać się po wyznaczonej trasie,
* określać swoją pozycję,
* zbierać dane z zamontowanych sensorów,
* komunikować się z systemem naziemnym,
* zapisywać wyniki pomiarów,
* reagować na zmiany warunków misji.

Docelowo kilka jednostek może wykonywać wspólną misję, a system może zmieniać ich zadania w przypadku wystąpienia problemów, np. utraty jednej z jednostek.

### Architektura

Projekt jest podzielony na trzy główne elementy:

```text
                         WAVE
                          │
          ┌───────────────┼───────────────┐
          │               │               │
         ASV             WMCP             WIC
          │               │               │
   jednostki nawodne   zarządzanie      konwersja
      i sensory          misją           danych
```

#### ASV — Autonomous Surface Vehicles

Fizyczna część systemu.

POC zakłada budowę niewielkich autonomicznych jednostek nawodnych. Konstrukcja jest projektowana jako katamaran z napędem różnicowym, wykorzystującym dwa niezależne silniki elektryczne.

Jednostki mają być wyposażone w komputer pokładowy typu SBC oraz odpowiednie sensory.

Planowane możliwości obejmują m.in.:

* autonomiczną nawigację,
* wykonywanie zaplanowanych tras,
* zbieranie danych środowiskowych,
* komunikację radiową,
* rejestrowanie danych z misji,
* obsługę różnych modułów pomiarowych.

W pierwszej kolejności system będzie rozwijany z wykorzystaniem możliwie prostego zestawu sensorów, np. pomiaru temperatury wody.

#### WMCP — WAVE Mission Control & Planning

Centralny system planowania i zarządzania misją.

WMCP ma umożliwiać:

* przygotowanie misji,
* importowanie danych geograficznych,
* definiowanie obszaru działania,
* generowanie lub ręczne definiowanie tras,
* monitorowanie jednostek,
* odbieranie danych z misji,
* wizualizację wyników,
* reagowanie na awarie i utratę jednostek,
* ponowne planowanie zadań pozostałych jednostek.

Dane geograficzne wykorzystywane podczas przygotowania misji nie muszą być częścią wewnętrznego formatu danych WAVE. WMCP może korzystać ze standardowych formatów GIS, takich jak **GeoJSON**, dzięki czemu dane przygotowane np. w QGIS mogą zostać bezpośrednio wykorzystane podczas planowania misji.

#### WIC — WAVE Interoperability Converter

Warstwa odpowiedzialna za konwersję danych zebranych podczas misji.

Dane wewnętrzne WAVE mogą być przekształcane do standardowych formatów, np.:

* CSV,
* JSON,
* innych formatów zależnie od potrzeb użytkownika.

WIC ma pozwalać na konfigurację m.in.:

* nazw pól,
* kolejności kolumn,
* jednostek,
* konwersji jednostek,
* metadanych,
* struktury pliku wyjściowego.

Celem jest umożliwienie wykorzystania danych WAVE w istniejących narzędziach analitycznych bez konieczności dostosowywania tych narzędzi do wewnętrznego formatu systemu.

---

## Dane geograficzne

WAVE nie ma na celu zastępowania oprogramowania GIS.

Przygotowanie danych geograficznych może odbywać się w istniejących, otwartych narzędziach, przede wszystkim w **QGIS**.

Przykładowy przepływ danych:

```text
Geoportal
   │
   ▼
BDOT10k / dane geograficzne
   │
   ▼
QGIS
   │
   ├── wybór obszaru
   ├── przygotowanie geometrii
   ├── utworzenie siatki / obszaru misji
   └── eksport
   │
   ▼
GeoJSON
   │
   ▼
WMCP
   │
   ▼
plan misji
```

Takie podejście pozwala wykorzystać istniejące standardy GIS zamiast tworzyć kolejny własny format danych geograficznych.

---

## Planowany scenariusz demonstracyjny

Pierwszym praktycznym zastosowaniem WAVE ma być autonomiczne mapowanie niewielkiego akwenu.

Jednostka lub jednostki otrzymują obszar działania oraz plan misji, następnie autonomicznie wykonują pomiary i przekazują dane do systemu naziemnego.

Przykładowy przebieg:

```text
         przygotowanie obszaru
                  │
                  ▼
              plan misji
                  │
                  ▼
              ┌───────┐
              │  ASV  │
              └───┬───┘
                  │
          autonomiczna misja
                  │
          ┌───────┴───────┐
          ▼               ▼
       pozycja          sensory
          │               │
          └───────┬───────┘
                  ▼
              dane misji
                  │
                  ▼
                WMCP
                  │
                  ▼
             WIC / eksport
```

W przypadku wielu jednostek system powinien również umożliwiać zmianę planu misji w trakcie jej wykonywania, np. po utracie jednej z jednostek.

---

## Możliwe zastosowania

Technologia rozwijana w ramach WAVE może być wykorzystana m.in. do:

* monitorowania zbiorników wodnych,
* pomiarów środowiskowych,
* mapowania obszarów wodnych,
* badań biologicznych,
* oceanografii,
* monitorowania portów,
* inspekcji infrastruktury wodnej,
* zastosowań poszukiwawczo-ratowniczych,
* automatycznego gromadzenia danych naukowych.

POC nie ma realizować wszystkich tych zastosowań. Mają one stanowić możliwe kierunki dalszego rozwoju systemu.

---

## Technologie

Projekt jest rozwijany przede wszystkim z wykorzystaniem:

* **Python** — oprogramowanie systemowe i narzędzia,
* **C/C++** — potencjalne komponenty niskopoziomowe,
* **Raspberry Pi / Orange Pi** — komputery pokładowe,
* **QGIS** — przygotowanie danych geograficznych,
* **GeoJSON** — wymiana danych geograficznych z WMCP,
* **CAD / druk 3D** — projektowanie i wykonanie konstrukcji ASV.

Dokładny dobór komponentów sprzętowych może ulec zmianie w trakcie rozwoju projektu.

---

## Status projektu

**Status: Proof of Concept / aktywny rozwój**

Projekt jest rozwijany etapami. Priorytetem jest najpierw uzyskanie działającej, możliwie prostej jednostki oraz podstawowego łańcucha:

```text
dane geograficzne
        ↓
      WMCP
        ↓
   planowanie misji
        ↓
       ASV
        ↓
   dane pomiarowe
        ↓
      WMCP
        ↓
       WIC
        ↓
   dane użytkownika
```

Dalsze funkcje, takie jak współpraca wielu jednostek, dynamiczne przeplanowanie misji czy większa liczba sensorów, będą rozwijane po osiągnięciu działającej wersji podstawowej.

---

## Roadmap

* [ ] podstawowy model ASV
* [ ] sterowanie napędem
* [ ] komputer pokładowy
* [ ] podstawowa komunikacja
* [ ] autonomiczne wykonywanie trasy
* [ ] podstawowy sensor pomiarowy
* [ ] WMCP — podstawowe planowanie misji
* [ ] import GeoJSON
* [ ] wizualizacja misji
* [ ] rejestrowanie danych
* [ ] WIC — podstawowy eksport danych
* [ ] testy na akwenie
* [ ] obsługa wielu ASV
* [ ] dynamiczne przeplanowanie misji
* [ ] dodatkowe moduły pomiarowe

---

## Założenia projektu

WAVE jest rozwijany z naciskiem na:

**Modułowość** — elementy systemu powinny być możliwie łatwe do wymiany i rozwijania.

**Otwarte standardy** — tam, gdzie jest to możliwe, projekt wykorzystuje istniejące standardy zamiast tworzyć własne rozwiązania bez wyraźnej potrzeby.

**Niski koszt** — POC ma być możliwy do wykonania przy ograniczonym budżecie.

**Reprodukowalność** — konstrukcja i oprogramowanie powinny umożliwiać innym osobom odtworzenie lub rozwinięcie systemu.

**Rozdzielenie odpowiedzialności** — nawigacja, zarządzanie misją, dane geograficzne i przetwarzanie wyników nie powinny być niepotrzebnie połączone w jeden komponent.

---

## Status dokumentacji

Projekt jest w trakcie rozwoju. Część opisanych tutaj funkcji stanowi planowaną funkcjonalność, a nie gotowe elementy systemu.

Nie należy traktować roadmapy jako listy funkcji już zaimplementowanych.

---

# 🇬🇧 English

# WAVE — Water Autonomous Vehicle Ecosystem

> **Autonomous surface vehicles for data collection and mission-based operations.**

WAVE (*Water Autonomous Vehicle Ecosystem*) is a project focused on autonomous surface vehicles (**ASVs**) and the software required to plan, manage and process data from their missions.

The goal is to develop an open and modular system that can use small autonomous surface vehicles to perform tasks that would otherwise require manual measurements or significantly more expensive equipment.

The project is currently being developed as a **Proof of Concept (POC)**.

---

## Core concept

WAVE combines autonomous surface vehicles with a computer-based mission management system.

In its basic form, an ASV should be able to:

* navigate along a predefined route,
* determine its position,
* collect data from onboard sensors,
* communicate with the ground system,
* record mission data,
* react to changes in mission conditions.

In a multi-ASV configuration, several vehicles can cooperate on the same mission, with the system potentially reallocating tasks if one of the vehicles becomes unavailable.

---

## Architecture

The project is divided into three main components:

```text
                         WAVE
                          │
          ┌───────────────┼───────────────┐
          │               │               │
         ASV             WMCP             WIC
          │               │               │
     surface vehicles   mission         data
       and sensors      control       conversion
```

### ASV — Autonomous Surface Vehicles

The physical part of the system.

The POC is planned around small autonomous surface vehicles. The current concept uses a catamaran configuration with differential thrust provided by two independent electric motors.

The vehicles are intended to use a single-board computer and modular sensors.

Planned capabilities include:

* autonomous navigation,
* predefined mission execution,
* environmental data collection,
* wireless communication,
* mission data logging,
* modular sensor support.

The initial system will use a deliberately simple sensor configuration, such as water temperature measurement.

### WMCP — WAVE Mission Control & Planning

The central mission planning and management system.

WMCP is intended to provide:

* mission preparation,
* geographic data import,
* operational area definition,
* route generation and manual route definition,
* vehicle monitoring,
* mission data collection,
* result visualization,
* failure and vehicle-loss handling,
* mission replanning.

Geographic data does not need to be part of WAVE's internal mission-data format. WMCP can use established GIS formats such as **GeoJSON**, allowing geographic data prepared in software such as QGIS to be directly used for mission planning.

### WIC — WAVE Interoperability Converter

The data conversion layer of WAVE.

Mission data collected by the vehicles can be converted into standard formats such as:

* CSV,
* JSON,
* other formats depending on user requirements.

WIC is intended to provide configurable:

* field names,
* column ordering,
* units,
* unit conversions,
* metadata,
* output structure.

The purpose is to make WAVE data usable with existing analysis tools without requiring those tools to understand WAVE's internal data representation.

---

## Geographic data

WAVE is not intended to replace GIS software.

Geographic data can be prepared using existing open-source tools, primarily **QGIS**.

A typical workflow can be:

```text
Geoportal
   │
   ▼
BDOT10k / geographic data
   │
   ▼
QGIS
   │
   ├── select area
   ├── process geometry
   ├── create mission area / grid
   └── export
   │
   ▼
GeoJSON
   │
   ▼
WMCP
   │
   ▼
mission plan
```

This approach allows WAVE to use established GIS standards instead of introducing another proprietary geographic data format.

---

## Demonstration scenario

The first practical WAVE application is planned as autonomous mapping of a small body of water.

The vehicle or vehicles receive an operational area and mission plan, autonomously perform measurements and transmit the collected data to the ground system.

A simplified workflow is:

```text
          area preparation
                  │
                  ▼
             mission plan
                  │
                  ▼
              ┌───────┐
              │  ASV  │
              └───┬───┘
                  │
          autonomous mission
                  │
          ┌───────┴───────┐
          ▼               ▼
       position         sensors
          │               │
          └───────┬───────┘
                  ▼
             mission data
                  │
                  ▼
                WMCP
                  │
                  ▼
             WIC / export
                  │
                  ▼
          user-readable data
```

With multiple vehicles, the system should also be capable of modifying the mission plan while the mission is underway, for example after losing one of the vehicles.

---

## Potential applications

The technology developed within WAVE could potentially be used for:

* water-body monitoring,
* environmental measurements,
* aquatic mapping,
* biological research,
* oceanographic research,
* port monitoring,
* water infrastructure inspection,
* search-and-rescue applications,
* automated scientific data collection.

The POC is not intended to implement all of these applications. They represent possible directions for future development.

---

## Technologies

The project is primarily developed using:

* **Python** — system software and tools,
* **C/C++** — potential low-level components,
* **Raspberry Pi / Orange Pi** — onboard computers,
* **QGIS** — geographic data preparation,
* **GeoJSON** — geographic data exchange with WMCP,
* **CAD / 3D printing** — ASV design and fabrication.

The exact hardware configuration may change during development.

---

## Project status

**Status: Proof of Concept / active development**

Development is being carried out incrementally. The immediate priority is to build a working, deliberately simple vehicle and establish the basic pipeline:

```text
geographic data
       ↓
     WMCP
       ↓
 mission planning
       ↓
      ASV
       ↓
 measurement data
       ↓
     WMCP
       ↓
      WIC
       ↓
 user data
```

More advanced capabilities, including multi-ASV cooperation, dynamic mission replanning and additional sensors, will be developed after the basic system is operational.

---

## Roadmap

* [ ] basic ASV prototype
* [ ] propulsion control
* [ ] onboard computer
* [ ] basic communication
* [ ] autonomous route execution
* [ ] basic measurement sensor
* [ ] WMCP — basic mission planning
* [ ] GeoJSON import
* [ ] mission visualization
* [ ] data logging
* [ ] WIC — basic data export
* [ ] water testing
* [ ] multi-ASV support
* [ ] dynamic mission replanning
* [ ] additional sensor modules

---

## Design principles

WAVE is being developed with an emphasis on:

**Modularity** — individual system components should be replaceable and extendable.

**Open standards** — established standards should be preferred over unnecessary custom formats.

**Low cost** — the POC should be achievable with limited funding.

**Reproducibility** — the hardware and software should allow others to reproduce or extend the system.

**Separation of responsibilities** — navigation, mission management, geographic data and result processing should not be unnecessarily coupled into a single component.

---

## Documentation status

WAVE is an active development project. Some features described above are planned functionality rather than implemented components.

The roadmap should therefore not be interpreted as a list of features that are already implemented.
