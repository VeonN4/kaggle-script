import os

jalanbokep = "/kaggle/working/x1101/models/Stable-diffusion"
tempatbokep = os.listdir(jalanbokep)
xtentacion = ['safetensors', 'pt']
nama_bokep = [nb for nb in tempatbokep
              if any(nb.endswith(ext) for ext in xtentacion)]

def kontol():
    print("List bokep:")
    for file_bokep in nama_bokep:
        print("-\t", file_bokep)
    hapus = input("Hapus bokep: ")
    penghapusbokep = os.path.join(jalanbokep, hapus)
    try:
        print(f"\nMenghapus bokep dengan nama {hapus}.")
        os.remove(penghapusbokep)
        print("Bokep terhapus")
    except FileNotFoundError:
        print(f"\nKami mencoba untuk menghapus bokep dengan nama {hapus} sir. \nTetapi bokep tidak di temukan sir. Mungkin tidak ada atau mungkin anda salah input sir. \n*Agen bokep kembali ke kantor.")  
    
kontol()