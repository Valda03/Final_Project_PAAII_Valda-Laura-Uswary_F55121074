Final Project PAA II
Valda Laura Uswary F55121074 (TI B)

Bubble Sort
Berdasarkan program sorting yang telah dilakukan dapat disimpulkan bawah algoritma bubble sort yang digunakan merupakan average case. Alasan utamanya adalah karena Bubble Sort memiliki kompleksitas waktu rata-rata O(n^2), di mana "n" adalah jumlah elemen dalam array yang diurutkan. jadi, pada best case, average case, dan worst case pada bubble sort semuanya memiliki kompleksitas waktu yang sama. Dalam average case, Bubble Sort memiliki kecenderungan untuk memerlukan banyak perbandingan dan pertukaran data ketika array tidak terurut dengan sempurna. Pada setiap iterasi, Bubble Sort melintasi seluruh array untuk membandingkan pasangan elemen. Jika terdapat elemen yang harus dipindahkan ke posisi yang benar, mereka akan bergeser satu per satu melalui array. Oleh karena itu, semakin besar ukuran array, semakin banyak waktu komputasi yang dibutuhkan. 
Pada best case, kompleksitas waktu O(n^2) terjadi ketika array sudah terurut secara menaik. Dalam kasus ini, Bubble Sort hanya akan melakukan satu iterasi untuk memastikan bahwa array sudah terurut. Namun, dalam implementasi umum Bubble Sort, hal ini sering tidak dioptimalkan, dan tetap memerlukan n-1 iterasi untuk menyelesaikan pengurutan.
Pada worst case, kompleksitas waktu O(n^2) terjadi ketika array belum terurut atau terurut secara terbalik, dan setiap elemen harus dipindahkan ke posisi yang benar dengan melakukan penukaran berulang. Dalam kasus ini, Bubble Sort akan melakukan n-1 iterasi pada setiap fase, dan setiap iterasi memerlukan perbandingan dan penukaran elemen. Misalnya, Bubble Sort memerlukan 74 iterasi untuk mengurutkan array dengan 75 elemen.

Insertion Sort
Berdasarkan program sorting yang telah dilakukan dapat disimpulkan bawah algoritma insertion sort yang digunakan merupakan average case. Karena array yang diurutkan tidak terurut secara terbalik atau terurut secara teratur. Pada kasus rata-rata, algoritma sorting seperti Insertion Sort akan melakukan operasi perbandingan dan penukaran elemen dengan jumlah yang sedang rata-rata.Jumlah pergeseran rata-rata yang diperlukan dalam Insertion Sort adalah sekitar n * (n-1) / 4, dan kompleksitas waktu rata-rata adalah O(n^2).
Best case pada algoritma Insertion Sort terjadi ketika array sudah dalam urutan yang terurut atau hampir terurut. Dalam kasus ini, setiap elemen hanya memerlukan sedikit pergeseran atau tidak perlu bergeser sama sekali. Dalam best case, kompleksitas waktunya adalah O(n) karena setiap elemen hanya perlu dibandingkan dengan elemen sebelumnya dalam satu iterasi.
Worst case pada algoritma Insertion Sort terjadi ketika array yang diurutkan berada dalam urutan terbalik. Pada kasus ini, setiap elemen harus bergeser ke posisi yang benar secara berurutan. Jumlah total pergeseran adalah sebanyak n * (n-1) / 2, di mana n adalah jumlah elemen dalam array. Oleh karena itu, pada worst case, kompleksitas waktunya adalah O(n^2).

Algoritma TSP (Traveling Salesman Problem)


Algoritma Djikstra
