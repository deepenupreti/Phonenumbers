import xlsxwriter

workbook = xlsxwriter.Workbook('Landline.xlsx')
worksheet = workbook.add_worksheet()

STD_codes = {
    'Achham' : '97',
    'Arghakhanchi' : '77',
    'Baglung' : '68',
    'Bandipur' : '100',
    'Banepa' : '11',
    'Bardiya' : '84',
    'Beni' : '69',
    'Besisahar' : '66',
    'Bhadrapur' : '23',
    'Bhairawaha' :'71',
    'Bhajani' : '91',
    'Bhaktapur' : '16',
    'Bharatpur' : '56',
    'Bhairahawa' : '71',
    'Bairghat' : '78',
    'Bhimphedi' : '57',
    'Bhojpur' : '29',
    'Bidur' : '10',
    'Biratnagar' : '21',
    'Birgung' : '51',
    'Birtamod' : '23',
    'Rupandehi' : '71',
    'Charikot' : '49',
    'Dadheldhura' : '96',
    'Damak' : '23',
    'Damauli' : '65',
    'Dang' : '82',
    'Darchula' : '93',
    'Dhading' : '10',
    'Dhangadi' : '91',
    'Dhankuta' : '26',
    'Dharan' : '25',
    'Dipayal' : '94',
    'Dodharachadani' : '99',
    'Doti' : '94',
    'Duhabi' : '25',
    'Gaighat' : '35',
    'Gaur' : '55',
    'Ghorahi' : '82',
    'Gorkha' : '64',
    'Guleria' : '84',
    'Gulmi' : '79',
    'Hetauda' : '57',
    'Ilam' : '27',
    'Inaruwa' : '25',
    'Itahari' : '21',
    'Jaleshwar' : '44',
    'Janakpur' : '41',
    'Kalaiya' : '53',
    'Katari' : '35',
    'Kathmandu' : '14',
    'Khadbari' : '29',
    'Khotang' : '36',
    'Khusma' : '67',
    'Krishnanagar' : '76',
    'Lahan' : '33',
    'Lalitpur' : '15',
    'Lumbini' : '71',
    'Lumjung' : '66',
    'Mahendranagar' : '99',
    'Malangawa' : '46',
    'Myagdi' : '69',
    'Nawalparasi' : '78',
    'Nepalgunj' : '81',
    'Okhaldhunga' : '37',
    'Palpa' : '75',
    'Panchthar' : '24',
    'Parasi' : '78',
    'Patan' : '1',
    'Phidim' : '24',
    'Pokhara' : '61',
    'Rajbiraj' : '31',
    'Rajpur' : '84',
    'Ramechap' : '48',
    'Rangeli' : '21',
    'Rasuwa' : '10',
    'Sandikharka' : '77',
    'Sankhuwasava' : '29',
    'Simra' : '53',
    'Sindhuli' : '47',
    'Siraha' : '33',
    'Surkhet' : '83',
    'Syanja' : '63',
    'Tandi' : '56',
    'Tansen' : '75',
    'Taplejung' : '24',
    'Taulihawa' : '76',
    'Terathum' : '26',
    'Tikapur' : '91',
    'Tribeni' : '78',
    'Trishuli' : '10',
    'Tulsipur' : '82',
    'Udaipur'  : '35',
}

row = 0
col = 0

for district,code in STD_codes.iteritems():
    worksheet.write(row, col, district)
    worksheet.write(row, col + 1, code)
    row += 1

workbook.close()
