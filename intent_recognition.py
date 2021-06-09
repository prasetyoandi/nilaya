from sentences import sentences #mengambil variabel dari file sentences

def getIntent(spell) :
    for sentence in sentences : # mencacah array pertama berupa daftar sentences
        for phrase in sentence['phrase'] : # mencacah daftar kalimat yang terdapat pada sentences 
            count = 0
            for word in spell.split(' ') : # mencacah kata yang diterima dari google
                if word in phrase : # melakukan pengecekan apakah kata yang diterima dari google terdapat pada sentences
                    count = count + 1
            if(count == len(phrase)) :
                return(sentence['event']) # jika menemukan yang sesuai, fungsi mengirimkan nilai balikan berupa event
    return None # jika tidak ada yang sesuai fungsi akan mengirim nilai balikan kosong