shi_do_list = {'서울':'서울특별시','부산':'부산광역시','대구':'대구광역시','인천':'인천광역시','광주':'광주광역시','대전':'대전광역시','울산':'울산광역시','세종':'세종특별자치도','경기':'경기도','강원':'강원도','충북':'충청북도','충남':'충청남도','전북':'전라북도','전남':'전라남도','경북':'경상북도','경남':'경상남도','제주':'제주특별자치도'}

adr1 = '경북 포항시 북구 장성동 1455-1'
adr2 = '경북 포항시 북구 흥해읍 이안리 424'
adr3 = '경북 경주시 북구 성건동 631-18'
adr1 = adr1.split(' ')
adr2 = adr2.split(' ')
adr3 = adr3.split(' ')

address = []
address.append(adr1)
address.append(adr2)
address.append(adr3)
# address[0]
for i in address:
    if i[0] in shi_do_list:
        print(shi_do_list[i[0]])