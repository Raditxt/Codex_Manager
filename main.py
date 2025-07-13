from codex.manager import CodexManager
from interface.cli import *

def main():
    manager = CodexManager()

    while True:
        print_menu()
        choice = input("Pilih opsi: ")

        if choice == "1":
            entry = input_entry()
            manager.add_entry(entry)
            print("✅ Entry ditambahkan.")
        elif choice == "2":
            for e in manager.list_all():
                display_entry(e)
        elif choice == "3":
            tag = input("Masukkan tag: ")
            results = manager.search_by_tag(tag)
            for e in results:
                display_entry(e)
        elif choice == "4":
            keyword = input("Masukkan judul: ")
            results = manager.search_by_title(keyword)
            for e in results:
                display_entry(e)
        elif choice == "5":
            title = input("Judul entry yang ingin dihapus: ")
            confirm =  input(f"Yakin hapus '{title}'? (y/n) : ")
            if confirm.lower() == 'y':
                manager.delete_entry(title)
                print("🗑️ Entry dihapus.")
        elif choice == "0":
            print("Sampai jumpa, Aether.")
            break
        else:
            print("Opsi tidak dikenali.")

if __name__ == "__main__":
    main()
