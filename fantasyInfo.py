# Football API
from distutils.log import debug
from espn_api.football import League

league = League(league_id=172798, year=2015, espn_s2="AEAv92zdOewoDRcfdj4%2BW%2BF5GYzRmKk50gzE5Ga5dYssofUHStH%2FbGHTJC%2FkGlKIywDWn3i%2BzYzaTWr2e3c7DnYoFU67GxlHN5NVAfyFQ%2Fnm7tAW1cm3EPOLi3kWDJQVtBCy7H5RKYRyQdd7Pl44qOwyx2sTOuXjBfm1WweU755JrhT7ZL4WmXoRKRoaEHgaSDszkcwGuRrcUwVtOVyXuewOi7k9aSHVM4qh925Uh1bWZMaxke9tk1eB2yeN0E5WUPcvGbMJPEZ3G9TFLYyL3PWC", swid='{8ADCD598-EF97-4F8F-9983-D8FE222E1248}', debug=False)

print(league.standings())

