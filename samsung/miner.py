from konlpy.tag import Okt

from nltk.tokenize import word_tokenize



@staticmethod

def read_file():
    okt = Okt()
    okt.pos("삼성전자 글로벌센터 전자사업부",stem=True)
    filename = 'data/kr-Report_2018.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        texts = f.read()

    @staticmethod
    def extract_hangul(texts):
        temp = texts.replace('\n',' ')
            tokenizer = re.compiler(r'[^ ㄱ-힣+')
            temp = tokenizer.sub('', temp)

            print(temp[:300])

@staticmethod

def change_token(texts):
    tokens = word_tokenize()
    print(tokens[:7])