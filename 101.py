solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','혜왕성','지구']
planet = '지구'
pos = solarsys.index(planet)
print('%s는 태양계에서 %d번째 위치' %(planet, pos))
pos = solarsys.index(planet,5)
print('%s는 태양계에서 %d번째 위치' %(planet, pos))
