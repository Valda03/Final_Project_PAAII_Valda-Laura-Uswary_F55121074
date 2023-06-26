import time
import sys

def tsp(graph, node_awal):
    awal = time.time()
    nodes = list(graph.keys())
    path = [node_awal]
    sisa_nodes = nodes.copy()
    sisa_nodes.remove(node_awal)

    path_terbaik = None
    jarak_terpendek = sys.maxsize

    def bnb(node_sekarang, jarak_sekarang, path_sekarang, sisa):
        nonlocal jarak_terpendek, path_terbaik


        if not sisa:
            if node_sekarang in graph and node_awal in graph[node_sekarang]:
                jarak = jarak_sekarang + graph[node_sekarang][node_awal]
                if jarak < jarak_terpendek:
                    jarak_terpendek = jarak
                    path_terbaik = path_sekarang + [node_awal]
            return

        for node in sisa:
            if node_sekarang in graph and node in graph[node_sekarang]:
                jarak = jarak_sekarang + graph[node_sekarang][node]

                sisa_copy = sisa.copy()
                sisa_copy.remove(node)

                bnb(node, jarak, path_sekarang + [node], sisa_copy)


    bnb(node_awal, 0, path, sisa_nodes)

    akhir = time.time()
    waktu_komputasi = akhir - awal

    if path_terbaik is not None:
        print("Iterasi Pemilihan Path TSP")
        for i in range(len(path_terbaik) - 1):
            node_sekarang = path_terbaik[i]
            node_selanjutnya = path_terbaik[i + 1]
            jarak = graph[node_sekarang][node_selanjutnya]
            print(f"Iterasi path ke-{i+1} = {node_sekarang} -> {node_selanjutnya} : Jarak = {jarak}")
            # print(f"Iterasi Path ke-{i+1} = {path} : Total Jarak = {total_distance}")

        print("\nPath Terpendek Yang Didapatkan (TSP)")
        for i in range(len(path_terbaik) - 1):
            print(f"{path_terbaik[i]} -> ", end="")
        print(path_terbaik[-1])
        print(f"Total Jarak : {jarak_terpendek}")
        print(f"Waktu Komputasi : {waktu_komputasi} detik")
    else:
        print("Tidak ditemukan solusi.")


def dijkstra(graph, node_awal, node_akhir):
    awal = time.time()
    belum_dikunjungi = set(graph.keys())

    jarak = {node: sys.maxsize for node in graph}
    jarak[node_awal] = 0

    jalur_terpendek = {node: [] for node in graph}


    while belum_dikunjungi:
        node_sekarang = min(belum_dikunjungi, key=lambda node: jarak[node])

        for tetangga, bobot in graph[node_sekarang].items():
            if tetangga in belum_dikunjungi:
                jarak_baru = jarak[node_sekarang] + bobot
                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru
                    jalur_terpendek[tetangga] = jalur_terpendek[node_sekarang] + [node_sekarang]

        belum_dikunjungi.remove(node_sekarang)

        if node_sekarang == node_akhir:
            break

    akhir = time.time()
    waktu_komputasi = akhir - awal

    print("Iterasi Pemilihan Path Dijkstra")
    jalur_terpilih = jalur_terpendek[node_akhir] + [node_akhir]
    jarak_total = 0
    for i in range(len(jalur_terpilih) - 1):
        node_sekarang = jalur_terpilih[i]
        next_node = jalur_terpilih[i + 1]
        jarak = graph[node_sekarang][next_node]
        jarak_total += jarak
        path = ' -> '.join(jalur_terpilih[:i+2])
        print(f"Iterasi Path ke-{i+1} = {path} : Total Jarak = {jarak_total}")

    print("\nPath Terpendek Yang Didapatkan (Dijkstra)")
    print("Path :", ' -> '.join(jalur_terpilih))
    print("Total Jarak :", jarak_total)
    print("Waktu Komputasi :", waktu_komputasi, "detik")

if __name__ == '__main__':
    graph = {
        'a': {'b': 12, 'c': 10, 'g': 12},
        'b': {'a': 12, 'd': 12, 'c': 8},
        'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
        'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
        'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
        'f': {'d': 10, 'e': 6, 'g': 9},
        'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
    }

    print("Pilihan Algoritma")
    print("1. TSP")
    print("2. Dijkstra")
    pilih = int(input("\nMasukkan Pilihan Anda (1-2) : "))

    if pilih == 1:
      node_awal = input("Masukkan Node Awal (a-g) : ")
      print()
      tsp(graph, node_awal)

    elif pilih == 2:
      node_awal = input("Masukkan Node Awal (a-g) : ")
      node_akhir = input("Masukkan Node Akhir (a-g) : ")
      print()
      dijkstra(graph, node_awal, node_akhir)

    else:
      print("Pilihan tidak valid")
