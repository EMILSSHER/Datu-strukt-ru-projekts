#ss.com auto sludinājumu apstrādes rīks
###Uzdevums:

Meklēt piemērotu automašīnu portālā ss.com var būt ilgs un nogurdinošs process, kā arī auto cenas bieži svārstās atkarībā no sezonas, izietas csdd skates vai citiem iemesliem. Tādēļ izveidojām programmu, kas automatizē meklēšanu un saglabā visus atrastos rezultātus excel failā, iesaka 3 labākos no tiem. Lietotājs ievada tikai sev interesējošos parametrus – marku, dzinēja tilpumu, ražošanas gadu un maksimālo cenu. Programma pati pārskata visus pieejamos sludinājumus ss.com portālā, un analizē piedāvājumus pēc to cenas, gada un nobraukuma attiecības un dod, mūsuprāt 3 labākos piedāvājumus.

###Izmantotās bibliotēkas:

selenium - Lapas automatizācijai un datu iegūšanai no ss.com
pandas -	Datu apstrādei un eksportam uz Excel
openpyxl	- galvenokārt, krāsošanai un attēlu pievienošanai
requests -	Attēlu lejupielādei no ss.com
uuid	- Unikālu id ģenerēšanai 
datetime -	Šodienas datuma noteikšanai
os -	Ceļš kur saglabāt excel failu un bilžu saglabāšanai
time	- Pauzes starp programmas pieprasījumiem
