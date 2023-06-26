Final Project PAA II
Valda Laura Uswary F55121074 (TI B)

Bubble Sort
Berdasarkan program sorting yang telah dilakukan dapat disimpulkan bawah algoritma bubble sort yang digunakan merupakan average case. Alasan utamanya adalah karena Bubble Sort memiliki kompleksitas waktu rata-rata O(n^2), di mana "n" adalah jumlah elemen dalam array yang diurutkan. jadi, pada best case, average case, dan worst case pada bubble sort semuanya memiliki kompleksitas waktu yang sama. Dalam average case, Bubble Sort memiliki kecenderungan untuk memerlukan banyak perbandingan dan pertukaran data ketika array tidak terurut dengan sempurna. Pada setiap iterasi, Bubble Sort melintasi seluruh array untuk membandingkan pasangan elemen. Jika terdapat elemen yang harus dipindahkan ke posisi yang benar, mereka akan bergeser satu per satu melalui array. Oleh karena itu, semakin besar ukuran array, semakin banyak waktu komputasi yang dibutuhkan. 
Pada best case, kompleksitas waktu O(n^2) terjadi ketika array sudah terurut secara menaik. Dalam kasus ini, Bubble Sort hanya akan melakukan satu iterasi untuk memastikan bahwa array sudah terurut. Namun, dalam implementasi umum Bubble Sort, hal ini sering tidak dioptimalkan, dan tetap memerlukan n-1 iterasi untuk menyelesaikan pengurutan.
Pada worst case, kompleksitas waktu O(n^2) terjadi ketika array belum terurut atau terurut secara terbalik, dan setiap elemen harus dipindahkan ke posisi yang benar dengan melakukan penukaran berulang. Dalam kasus ini, Bubble Sort akan melakukan n-1 iterasi pada setiap fase, dan setiap iterasi memerlukan perbandingan dan penukaran elemen. Misalnya, Bubble Sort memerlukan 74 iterasi untuk mengurutkan array dengan 75 elemen.

Insertion Sort
Berdasarkan program sorting yang telah dilakukan dapat disimpulkan bahwa algoritma insertion sort yang digunakan merupakan average case. Karena array yang diurutkan tidak terurut secara terbalik atau terurut secara teratur. Pada kasus rata-rata, algoritma sorting seperti Insertion Sort akan melakukan operasi perbandingan dan penukaran elemen dengan jumlah yang sedang rata-rata.Jumlah pergeseran rata-rata yang diperlukan dalam Insertion Sort adalah sekitar n * (n-1) / 4, dan kompleksitas waktu rata-rata adalah O(n^2).
Best case pada algoritma Insertion Sort terjadi ketika array sudah dalam urutan yang terurut atau hampir terurut. Dalam kasus ini, setiap elemen hanya memerlukan sedikit pergeseran atau tidak perlu bergeser sama sekali. Dalam best case, kompleksitas waktunya adalah O(n) karena setiap elemen hanya perlu dibandingkan dengan elemen sebelumnya dalam satu iterasi.
Worst case pada algoritma Insertion Sort terjadi ketika array yang diurutkan berada dalam urutan terbalik. Pada kasus ini, setiap elemen harus bergeser ke posisi yang benar secara berurutan. Jumlah total pergeseran adalah sebanyak n * (n-1) / 2, di mana n adalah jumlah elemen dalam array. Oleh karena itu, pada worst case, kompleksitas waktunya adalah O(n^2).


Algoritma TSP (Travelling Salesman Problem)
Berdasarkan program yang telah dibuat dapat disimpulkan bahwa algoritma TSP yang digunakan merupakan average case, karena graph node yang digunakan berbentuk acak, dimana jarak antara node-nya tidak teratur. Average Case pada TSP mengacu pada kinerja algoritma dalam skenario kasus yang umum atau acak, di mana node yang ada memiliki hubungan dan jarak yang tidak teratur. Rata-rata kompleksitas waktu algoritma TSP bergantung pada pendekatan yang digunakan. Algoritma yang lebih efisien seperti Dynamic Programming dengan pendekatan seperti Held-Karp atau algoritma approximasi dengan faktor konstan (seperti 2-approximation) biasanya memiliki kompleksitas waktu rata-rata yang lebih baik daripada pendekatan brute force. Dalam average case, algoritma dengan kompleksitas waktu O(N^2), O(N log N), atau O(N^3) masih dapat memberikan solusi yang memadai dengan waktu yang dapat diterima.
Best Case pada TSP terjadi ketika terdapat struktur node yang teratur atau simetris. Misalnya, jika seluruh node membentuk bentuk geometris tertentu, seperti lingkaran atau persegi, maka rute optimalnya akan memiliki pola yang teratur. Dalam best case, algoritma seperti Nearest Neighbor atau MST (Minimum Spanning Tree) yang menggunakan heuristik, dapat mencapai solusi yang mendekati optimal dengan kompleksitas waktu yang lebih baik dari worst case. Kompleksitas waktu untuk best case pada algoritma TSP yang efisien biasanya dinyatakan dengan O(N^2), O(N log N), atau O(N^3), tergantung pada teknik yang digunakan.
Worst Case pada TSP terjadi ketika jumlah node yang dikunjungi semakin banyak. Dalam worst case, jumlah permutasi rute yang harus diperiksa akan tumbuh secara faktorial dengan jumlah node. Oleh karena itu, worst case TSP memiliki kompleksitas waktu eksponensial, yaitu O(N!). Algoritma seperti Brute Force atau Backtracking yang secara eksplisit memeriksa semua kemungkinan permutasi rute, akan memiliki kinerja yang sangat buruk dalam worst case.

Algoritma Djikstra
Berdasarkan program yang telah dibuat dapat disimpulkan bahwa algoritma Dijkstra yang digunakan merupakan average case, karena pada kasus graph yang ada pada program, tidak ada indikasi bahwa graph memiliki struktur node yang sangat jarang atau sangat padat dan juga node awal serta tujuan terhubung melalui beberapa edge. Average Case pada algoritma Dijkstra terjadi ketika graph memiliki distribusi node dan edge yang acak. Dalam kasus ini, kompleksitas waktu Dijkstra dapat dianggap sama dengan kompleksitas waktu pada worst case yaitu O((V + E) log V). Meskipun average case sulit untuk didefinisikan secara pasti, kompleksitas ini memberikan perkiraan yang baik untuk sebagian besar graph dengan distribusi acak.
Best Case pada algoritma Dijkstra terjadi ketika terdapat hanya sedikit node dan edge dalam graph. Jika graph hanya terdiri dari satu node, maka algoritma Dijkstra akan langsung mencapai solusi tanpa melakukan iterasi atau perhitungan tambahan. Kompleksitas waktu dalam best case dapat dinyatakan sebagai O(V), di mana V adalah jumlah node dalam graph. Dalam best case, algoritma Dijkstra dapat memberikan solusi dengan kinerja yang sangat baik dan efisien.
Worst Case pada algoritma Dijkstra terjadi ketika graph memiliki banyak node dan banyak edge yang saling terhubung dengan bobot yang bervariasi. Dalam worst case, kompleksitas waktu algoritma Dijkstra adalah O((V + E) log V), di mana V adalah jumlah node dalam graph dan E adalah jumlah edge-nya. Worst Case terjadi ketika setiap node terhubung dengan setiap node lainnya melalui edge, sehingga jumlah edge adalah maksimum. Kompleksitas waktu pada worst case menunjukkan bahwa algoritma Dijkstra akan memiliki kinerja yang buruk dalam worst case dengan kompleksitas waktu yang meningkat secara linear terhadap jumlah node dan edge dalam graph.
