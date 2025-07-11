from codex.entry import Entry

def print_menu():
    print("\n=== AI Codex Manager ===")
    print("1. Tambah Entry")
    print("2. Lihat Semua")
    print("3. Cari berdasarkan Tag")
    print("4. Cari berdasarkan Judul")
    print("5. Hapus Entry")
    print("0. Keluar")

def input_entry():
    title = input("Judul: ")
    category = input("Kategori: ")
    tags = input("Tags (pisahkan dengan koma): ").split(",")
    tags = [t.strip() for t in tags if t.strip()]
    summary = input("Ringkasan: ")
    code_snippet = input("Kode (opsional): ")
    source = input("Sumber: ")
    return Entry(title, category, tags, summary, code_snippet, source)

def display_entry(entry):
    print("\n---")
    print(f"📝 Judul       : {entry.title}")
    print(f"📚 Kategori    : {entry.category}")
    print(f"🏷️ Tags        : {', '.join(entry.tags)}")
    print(f"📖 Ringkasan   : {entry.summary}")
    print(f"💻 Kode        : {entry.code_snippet}")
    print(f"🔗 Sumber      : {entry.source}")
    print(f"🕒 Dibuat      : {entry.date_created}")
