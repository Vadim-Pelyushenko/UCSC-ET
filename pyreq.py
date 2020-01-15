import bs4, requests

def get_result_list(rec_start, rec_dur):
	url = 'https://pisa.ucsc.edu/class_search/index.php'

	payload = f'action=update_segment&binds%5B%3Aterm%5D=2200&binds%5B%3Areg_status%5D=all&binds%5B%3Asubject%5D=&binds%5B%3Acatalog_nbr_op%5D=%3D&binds%5B%3Acatalog_nbr%5D=&binds%5B%3Atitle%5D=&binds%5B%3Ainstr_name_op%5D=%3D&binds%5B%3Ainstructor%5D=&binds%5B%3Age%5D=&binds%5B%3Acrse_units_op%5D=%3D&binds%5B%3Acrse_units_from%5D=&binds%5B%3Acrse_units_to%5D=&binds%5B%3Acrse_units_exact%5D=&binds%5B%3Adays%5D=&binds%5B%3Atimes%5D=&binds%5B%3Aacad_career%5D=&binds%5B%3Asession_code%5D=&rec_start={rec_start}&rec_dur={rec_dur}'
	headers = {
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Origin': 'https://pisa.ucsc.edu',
		'Upgrade-Insecure-Requests': '1',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
		'Sec-Fetch-User': '?1',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'navigate',
		'Referer': 'https://pisa.ucsc.edu/class_search/index.php',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9'
	}

	response = requests.request('POST', url, headers=headers, data=payload)
	webpage = response.text.encode('utf8')
	result_list = []

	soup = bs4.BeautifulSoup(webpage, features='html.parser')
	for row1 in soup.find_all(class_='panel panel-default row'):
		result_row = [row1.find_all(class_='panel-heading panel-heading-custom')[0].text]
	
		for row2 in row1.find_all(class_='col-xs-6 col-sm-3'):
			result_row.append(row2.text)
	
		for row2 in row1.find_all(class_='col-xs-12 col-sm-6'):
			for row3 in row2.find_all(class_='col-xs-6 col-sm-6'):
				result_row.append(row3.text)

		result_list.append(result_row)
	return result_list

if __name__ == '__main__':
	print(get_result_list(0, 100))
