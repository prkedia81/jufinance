import gspread

gc = gspread.service_account('./config.json')
sheet = gc.open_by_key('1YnjqZ2Rh7Z6pLImD1oHVh35eDKRze8ZjawonvGliIJI')
worksheet = sheet.sheet1
print(worksheet)
