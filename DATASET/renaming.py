import os

# Define the list of Hindi characters and their English transliterations
hindi_characters = ['क ', 'का ', 'कि ', 'की ', 'कु ', 'कू ', 'के ', 'कै ', 'को ', 'कं ',
                    'ख ', 'खा ', 'खि ', 'खी ', 'खु ', 'खू ', 'खे ', 'खै ', 'खो ', 'खं ',
                    'ग ', 'गा ', 'गि ', 'गी ', 'गु ', 'गू ', 'गे ', 'गै ', 'गो ', 'गं ',
                    'घ ', 'घा ', 'घि ', 'घी ', 'घु ', 'घू ', 'घे ', 'घै ', 'घो ', 'घं ',
                    'च ', 'चा ', 'चि ', 'ची ', 'चु ', 'चू ', 'चे ', 'चै ', 'चो ', 'चं ',
                    'छ ', 'छा ', 'छि ', 'छी ', 'छु ', 'छू ', 'छे ', 'छै ', 'छो ', 'छं ',
                    'ज ', 'जा ', 'जि ', 'जी ', 'जु ', 'जू ', 'जे ', 'जै ', 'जो ', 'जं ',
                    'झ ', 'झा ', 'झि ', 'झी ', 'झु ', 'झू ', 'झे ', 'झै ', 'झो ', 'झं ',
                    'ट ', 'टा ', 'टि ', 'टी ', 'टु ', 'टू ', 'टे ', 'टै ', 'टो ', 'टं ',
                    'ठ ', 'ठा ', 'ठि ', 'ठी ', 'ठु ', 'ठू ', 'ठे ', 'ठै ', 'ठो ', 'ठं ',
                    'ड ', 'डा ', 'डि ', 'डी ', 'डु ', 'डू ', 'डे ', 'डै ', 'डो ', 'डं ',
                    'ढ ', 'ढा ', 'ढि ', 'ढी ', 'ढु ', 'ढू ', 'ढे ', 'ढै ', 'ढो ', 'ढं ',
                    'ण ', 'णा ', 'णि ', 'णी ', 'णु ', 'णू ', 'णे ', 'णै ', 'णो ', 'णं ',
                    'त ', 'ता ', 'ति ', 'ती ', 'तु ', 'तू ', 'ते ', 'तै ', 'तो ', 'तं ',
                    'थ ', 'था ', 'थि ', 'थी ', 'थु ', 'थू ', 'थे ', 'थै ', 'थो ', 'थं ',
                    'द ', 'दा ', 'दि ', 'दी ', 'दु ', 'दू ', 'दे ', 'दै ', 'दो ', 'दं ',
                    'ध ', 'धा ', 'धि ', 'धी ', 'धु ', 'धू ', 'धे ', 'धै ', 'धो ', 'धं ',
                    'न ', 'ना ', 'नि ', 'नी ', 'नु ', 'नू ', 'ने ', 'नै ', 'नो ', 'नं ',
                    'प ', 'पा ', 'पि ', 'पी ', 'पु ', 'पू ', 'पे ', 'पै ', 'पो ', 'पं ',
                    'फ ', 'फा ', 'फि ', 'फी ', 'फु ', 'फू ', 'फे ', 'फै ', 'फो ', 'फं ',
                    'ब ', 'बा ', 'बि ', 'बी ', 'बु ', 'बू ', 'बे ', 'बै ', 'बो ', 'बं ',
                    'भ ', 'भा ', 'भि ', 'भी ', 'भु ', 'भू ', 'भे ', 'भै ', 'भो ', 'भं ',
                    'म ', 'मा ', 'मि ', 'मी ', 'मु ', 'मू ', 'मे ', 'मै ', 'मो ', 'मं ',
                    'य ', 'या ', 'यि ', 'यी ', 'यु ', 'यू ', 'ये ', 'यै ', 'यो ', 'यं ',
                    'र ', 'रा ', 'रि ', 'री ', 'रु ', 'रू ', 'रे ', 'रै ', 'रो ', 'रं ',
                    'ल ', 'ला ', 'लि ', 'ली ', 'लु ', 'लू ', 'ले ', 'लै ', 'लो ', 'लं ',
                    'व ', 'वा ', 'वि ', 'वी ', 'वु ', 'वू ', 'वे ', 'वै ', 'वो ', 'वं ',
                    'श ', 'शा ', 'शि ', 'शी ', 'शु ', 'शू ', 'शे ', 'शै ', 'शो ', 'शं ',
                    'स ', 'सा ', 'सि ', 'सी ', 'सु ', 'सू ', 'से ', 'सै ', 'सो ', 'सं ',
                    'ह ', 'हा ', 'हि ', 'ही ', 'हु ', 'हू ', 'हे ', 'है ', 'हो ', 'हं ',
                    'ष','षा',' षि',' षी',' षु ','षू ','षे ','षै ','षो ','षं',
                    'अ ', 'आ ', 'इ ', 'उ ', 'ए ', 'ओ ']

english_transliterations = ['ka', 'kaa', 'ki', 'kee', 'ku', 'koo', 'ke', 'kai', 'ko', 'kam',
                            'kha', 'khaa', 'khi', 'khee', 'khu', 'khoo', 'khe', 'khai', 'kho', 'kham',
                            'ga', 'gaa', 'gi', 'gee', 'gu', 'goo', 'ge', 'gai', 'go', 'gam',
                            'gha', 'ghaa', 'ghi', 'ghee', 'ghu', 'ghoo', 'ghe', 'ghai', 'gho', 'gham',
                            'cha', 'chaa', 'chi', 'chee', 'chu', 'choo', 'che', 'chai', 'cho', 'cham',
                            'chha', 'chhaa', 'chhi', 'chhee', 'chhu', 'chhoo', 'chhe', 'chhai', 'chho', 'chham',
                            'ja', 'jaa', 'ji', 'jee', 'ju', 'joo', 'je', 'jai', 'jo', 'jam',
                            'jha', 'jhaa', 'jhi', 'jhee', 'jhu', 'jhoo', 'jhe', 'jhai', 'jho', 'jham',
                            'ta', 'taa', 'ti', 'tee', 'tu', 'too', 'te', 'tai', 'to', 'tam',
                            'tha', 'thaa', 'thi', 'thee', 'thu', 'thoo', 'the', 'thai', 'tho', 'tham',
                            'da', 'daa', 'di', 'dee', 'du', 'doo', 'de', 'dai', 'do', 'dam',
                            'dha', 'dhaa', 'dhi', 'dhee', 'dhu', 'dhoo', 'dhe', 'dhai', 'dho', 'dham',
                            'na', 'naa', 'ni', 'nee', 'nu', 'noo', 'ne', 'nai', 'no', 'nam',
                            'pa', 'paa', 'pi', 'pee', 'pu', 'poo', 'pe', 'pai', 'po', 'pam',
                            'pha', 'phaa', 'phi', 'phee', 'phu', 'phoo', 'phe', 'phai', 'pho', 'pham',
                            'ba', 'baa', 'bi', 'bee', 'bu', 'boo', 'be', 'bai', 'bo', 'bam',
                            'bha', 'bhaa', 'bhi', 'bhee', 'bhu', 'bhoo', 'bhe', 'bhai', 'bho', 'bham',
                            'ma', 'maa', 'mi', 'mee', 'mu', 'moo', 'me', 'mai', 'mo', 'mam',
                            'ya', 'yaa', 'yi', 'yee', 'yu', 'yoo', 'ye', 'yai', 'yo', 'yam',
                            'ra', 'raa', 'ri', 'ree', 'ru', 'roo', 're', 'rai', 'ro', 'ram',
                            'la', 'laa', 'li', 'lee', 'lu', 'loo', 'le', 'lai', 'lo', 'lam',
                            'va', 'vaa', 'vi', 'vee', 'vu', 'voo', 've', 'vai', 'vo', 'vam',
                            'sha', 'shaa', 'shi', 'shee', 'shu', 'shoo', 'she', 'shai', 'sho', 'sham',
                            'sa', 'saa', 'si', 'see', 'su', 'soo', 'se', 'sai', 'so', 'sam',
                            'ha', 'haa', 'hi', 'hee', 'hu', 'hoo', 'he', 'hai', 'ho', 'ham',
                            'sha', 'shaa', 'shi', 'shee', 'shu', 'shoo', 'she', 'shai', 'sho', 'sham',
                            'a', 'aa', 'i', 'u', 'e', 'o']

# Replace Hindi characters in the folder name with their English transliterations
folder_name = 'd1'  # Update this with your folder name
for hindi_char, english_char in zip(hindi_characters, english_transliterations):
    folder_name = folder_name.replace(hindi_char.strip(), english_char)

# Rename the folder
os.rename('D:\\CDAC\\BramhaNetra\\DATASET\\' + 'SET1', 'D:\\CDAC\\BramhaNetra\\DATASET\\' + folder_name)
