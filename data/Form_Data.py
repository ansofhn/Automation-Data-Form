# Import module
from time import sleep as wait
import pandas as pd
import numpy as np
try: 
	from playsound import playsound
except: pass
# Function for called file mp3 with playsound module
def voice (mp3):
	try: playsound(mp3)
	except: pass
# Variabels
nama,kelas,asal,data = [],[],[],[]
voice('mulai.mp3')
while True :
    print("\n","="*10,"<< FORM DATA >>","="*10)
    print ("\n1. Masukan Data\n2. Tampilkan Data\n3. Hapus Data\n4. Save Data\n0. Exit")
    pilihan = int(input("\n|> Masukan pilihan anda: "))

    if pilihan == 1 :
        voice('masuk.mp3')
        print('\n'+'='*50+'>')
        inputNama = input("|> Nama Lengkap          : ")
        nama.append({'nama' : inputNama})
        inputKelas = input("|> Kompetensi Keahlian   : ")
        kelas.append({'kelas': inputKelas})
        inputAsal = input("|> Asal Sekolah          : ")
        asal.append({'asal' : inputAsal})
        print('='*50+'>')
        voice('proses.mp3')
        print("\n----< Data Telah Tersimpan >----\n"),voice('simpan.mp3')
        wait(1)

    elif pilihan == 2 :
        Kls,Name,From = [],[],[]
        voice('tampil.mp3')
        print('\n<<----<< DAFTAR BIODATA >>---->>\n')
        for i in range (len(kelas)):
            Name.append(nama[i]['nama'])
            Kls.append(kelas[i]['kelas'])
            From.append(asal[i]['asal'])
        data = list(zip(Name,Kls,From))
        column = " Nama Siswa "," Kompetensi Keahlian "," Asal Sekolah "
        Index = np.arange(1,(len(kelas)+1))
        Final_Data = pd.DataFrame(data,index=Index,columns=column)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        wait(1)
        print(Final_Data)
        wait(2)
        
    elif pilihan == 3 :
        voice('hapus.mp3')
        inputNama = input("\n|> Masukan nama : ")
        voice('proses.mp3')
        for i in range (len(nama)) :
            if inputNama == nama[i]['nama'] :
                print ("\n----< Data telah Terhapus >----")
                del kelas[i]
                del nama[i]
                del asal[i]
                wait(2)
            else: pass
        voice('del.mp3')
    elif pilihan == 4 :
        wait(2)
        print('\n---<< Data Saved in your Document.. >>---'),voice('simpan.mp3')
        Final_Data.to_csv('Result.csv')
    elif pilihan == 0 :
        print("\n---<< Terima Kasih telah menggunakan Program ini >>---"),voice('thank.mp3')
        wait(1),print('.'),wait(1),print('.'),wait(1),voice('end.mp3')
        print("Program Ended..")
        wait(1)
        break
