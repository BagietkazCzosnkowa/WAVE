#WAVE
[[pl]]

---
# !!!UWAGA!!!

Poradnik na dzień dzisiejszy obsługuje wyłącznie  Polskę i oprogramowanie QGIS. W przyszłości planowane jest dodanie innych krajów i innych programów.

---
# 1. Przygotowanie środowiska
 1. Zainstaluj program QGIS, jest on wymagany w tym porandiku. 
	[Oficjalna strona pobierania QGIS](https://qgis.org/resources/installation-guide/)
	Nie potrzebujesz żadnego dodatkowego oprogramowania. 
	Nie potrzebujesz przechodzić oficjalnych poradników QGIS, ten poradnik przeprowadzi cię krok po kroku po wszystkch kolejnych kliknięciach. QGIS to bardzo zaawansowane środowisko, na potrzeby WMCP nie potrzeba się go uczyć, użyjemy tylko niewielkiej części jego funkcji.
 2. Włącz QGIS. Po włączeniu powinien wyglądać mniej więcej tak:
 
   ![](./images/pl-tutorials/QGIS-look.png)

# 2. Zainstaluj wtyczkę BDOT10k

 1. Na górnym pasku kliknij Plugins -> Manage and Insall Plugins...
   Wyświetli się takie okienko:
   
   ![](./images/pl-tutorials/Plugins-Manage-and-Install.png)
   
 2. W pole *Search ...* należy pisać BDOT10k i wbrać plugin o dokładnie tej nazwie. Autorem jest Maryla Jeż.
 
   ![](./images/pl-tutorials/BDOT10k-plugin.png)
   
 3. Zainstaluj ten plugin i zamknij to okno, nie będziemy potrzebować więcej. 
BDOT10k to Baza Danych Obiektów Terenowych w skali 1:10 000. Są to oficjalne dane udostepniane przez Główny Urząd Geodezji i Kartografii. Ten plugin to jeden ze sposobów, na pobranie ich. 
# 3. Pobierz paczkę BDOT10k.
Teraz musimy pobrać odpoweidnie dane. 
1. U Na pasku górnmym pojawiły sie dwa przyciski, na zdjęciu zaznaczone czerwonym kólkiem.
   ![](./images/pl-tutorials/QGIS-with-BDOT10k-plugin.png)
   
   Otworzy się wtedy kolejne okno, należy tam wybrać interesujący nas powiat/powiaty.  U mnie wbieram część pojezierza warmińsko-mazurskiego. 
   
2. ![](./images/pl-tutorials/BDOT10k-plugin-data-download.png)
   Wybierczie folder pobierania danych. Ważne, żeby wybrać u góry opcję GPKG. 
   Kliknij oppcję "Pobierz". Pobierze to folder/y .zip, należy go/je rozpakować
3. Uwaga, po rozpakowaniu paczki .gpkg mają dość pokaźne rozmiary. Dla przykładu te cztery powiaty któ©e pobrałem to około 900MB. NA szczęście nie potrzebyjemy tego wszystkiego. Potrzebujemy z każdej paczki tylko kilku konkretnych wartw, resztę można usunąć. Potrzebujemy konkretnie:
	- PL.PZGiK.341.BDOT10k.XXXX_OT_SWRS_L - sieć wodna - rzeki
	- PL.PZGiK.341.BDOT10k.XXXX_OT_SWKN_L - sieć wodna - kanały
	- PL.PZGiK.341.BDOT10k.XXXX_OT_SWRM_L - sieć wodna - rowy melioracyjne
	- PL.PZGiK.341.BDOT10k.XXXX_OT_PTWP_A - pokrycie tereny - wodą powierzchniową (Najważniejsze)
Reszę można spokojnie usunąć, nie są do niczego potrzebne w tym przypadku.
Oto krótki skrytp w bash który usunie pozostałe pliki poza tymi czterema.

`find . -maxdepth 1 -type f ! -name '*_OT_SWRS_L*' ! -name '*_OT_SWKN_L*' ! -name '*_OT_SWRM_L*' ! -name '*_OT_PTWP_A*' -delete`

Aby go urzyć należy odpalić konsolę w Linuxie, wejść do katalogu w którym znajdują się rozpakowane pliki i wkleić w konsolę ten kod. 

Wersja PowerShell (Konsoli Windows):

`Get-ChildItem -File | Where-Object { $_.Name -notlike '*_OT_SWRS_L*' -and $_.Name -notlike '*_OT_SWKN_L*' -and $_.Name -notlike '*_OT_SWRM_L*' -and $_.Name -notlike '*_OT_PTWP_A*' } | Remove-Item`

# 4. Przugotuj projekt. 
W QGIS kliknij dwa razy w New Empty Project.  Wyświetli się taki widok:

![](./images/pl-tutorials/QGIS-empty-project.png)

Następnie w górnym pasku wybierz opcję Layer -> Add Layer -> Add Vector Layer. 

![](./images/pl-tutorials/QGIS-adding-layer.png)

Pojawi się wtedy takie okienko:

![](./images/pl-tutorials/QGIS-add-layer.png)

W okienku Vector Dataset(s), kliknij trzy kropeczki i wybierz wszystkie potrzebne ci pliki gpkg, tokładnie te z tymi z dopiskami, które wypisałem wyżej. Potem kliknij Add i Close.
Powtóż to dla każdego folderu.

Następnie na panelu po lewej kliknij XYZ Tiles -> OpenStreetMap (2 razy). Powinna się wyświetlić mapa podkłądkowa OSM , jednak nałożona NA wszystki warstwy niżej.

![](./images/pl-tutorials/QGIS-OSM-map.png)

Aby ustawić to prawidłowo, kliknij View -> Panels i zaznacz Layers.
Wyskoczy okienko, należy przesunąć warstwę OpenStreetMap na sam dół.

![](./images/pl-tutorials/QGIS-Layer-Manager.png)

# 5. Obróbka danych i dokładne przygotowanie misji

Dalej pokaże to na przykładzie jeziora Gołdapiwo. 

Porównaj kolor wybranego przez ciebie jeziora/rzeki/innego zbiornika wodnego/ i wybierz go na liście w panelu Layers. 
Następnie na panelu górnym zaznacz ikonkę Select Features by Area or Single Click i kliknij na to jezioro, powinno zmienić kolor na żółty.

![](./images/pl-tutorials/QGIS-lake-choosing.png)

Następnie kliknij prawym przyciskiem myszy na zaznaczoną warstwę, wybierz Export -> Save Selected Features As ...

![](./images/pl-tutorials/QGIS-lake-export.png)

Nazwij plik jakkolwiek, jednak sugeruję nazwę 'mission_area'.
Przesuń ją na samą górę. 

Następnie upewnij się, że mission_area jest zaznaczona (żółta) i kliknij po kolei Vector- Geoprocessing Tolls -> Buffer
Wyskoczy okienko specyfikacji buforu, proponuję takie ustawienia:
- Distance: -10m
- Segments: 20
- Dissolve: zaznaczone
- Reszty nie zmieniaj.

![](./images/pl-tutorials/Buffer-settings.png)

I zamknij okno.

Następnie zaznacz warstwę buforu, i w panelu warstw i na mapie, i kliknij Vector -> Reaserch Tools -> Create Grid. Sugeruję zastępujące ustawienia:
- Grid Extent: Wybierz Buffered, albo jakkolwiek nazwałeś warstwę ma której jest bufor.
- Horizontal/Vertical Spaceing: 25 m. (dla mniejszych punktów pomiarowych będzie niewiarygodnie dużo)
- Upewnij się, że Grid CRS to ESPG:2180
- Reszty nie zmieniaj

![](./images/pl-tutorials/Grid-Settings.png)

Zamknij okno.

Pojawią się punkty, ale na planie sześciokąta, a nie tylko na terenie jeziora. Trzeba teraz usunąć te poza jeziorem. 

![](./images/pl-tutorials/point-unfilterd.png)

Kliknij po kolei Vector -> Geoprocessing Tools -> Intersection
Ustaw 
- Input Layer: Grid (albo inną nazwę którą nadałeś siatce punktów)
- Overlay Layer: Bufferes (albo inną nazwę którą nadałeś siatce punktów)
I kliknij Run. UWAGA, to może trochę potrwać.

![](./images/pl-tutorials/Intersection-Points.png)

Już w zasadzie gotowe, pozostaje tylko wyeksportować odpowiednie dane, to jest warstwy Intersection, mission_area i buffered. 