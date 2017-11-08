import requests,os,argparse
from bs4 import BeautifulSoup
import urllib.parse
#using the website of https://zhongwenzhuanpinyin.51240.com

def text2spell(filename):
	txt_load='./resource/text/'+filename + '.txt'
	txt_name='./resource/Spell/'+filename + '.txt'
	file=open(txt_load, 'r')
	filedata = file.read()
	file.close()
	w=[]
	#send request
	payload = {
		'zwzyp_zhongwen':filedata,
		'zwzyp_shengdiao':'0',
		'zwzyp_wenzi':'1',
		'zwzyp_jiange':'1',
		'zwzyp_duozhongduyin':'1'
	}
	urllib.parse.urlencode(payload) 
	res=requests.post("https://zhongwenzhuanpinyin.51240.com/web_system/51240_com_www/system/file/zhongwenzhuanpinyin/data/?ajaxtimestamp=1509353694634",data=payload,headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	})
	file=open(txt_name, 'w')
	#split and save the result 
	soup=BeautifulSoup(res.text,'lxml')
	translate=soup.find_all('',{'class':'xiaokuang_py'})
	for translates in translate:
		w.append(translates.string.split('(')[0])
	sent=' '.join(w)
	print('result is: '+sent)
	file.write(sent)
	file.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='the txt file you want to translate')
	parser.add_argument("file_name")
	args = parser.parse_args()
	f=args.file_name.split('.')[0]
	text2spell(f)
	#for folder path
	'''
	#setting path
	path = "./resource/text"
	files = os.listdir( path )
	#find your mp3 file
	for file in files:
		f=file.split('.')[0]
		text2spell(f)
	'''


