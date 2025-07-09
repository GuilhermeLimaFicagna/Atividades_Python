import urllib
import urllib.request
try:
    st = urllib.request.urlopen("https://github.com/GuilhermeLimaFicagna")
except:
    print('\033[0;31mERRO\033[m')
else:
    print('\033[0;32mTudo certo\033[m')
