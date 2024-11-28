const div = document.querySelectorAll('div'); // mengambil semua elemen div
const li = document.querySelectorAll('li'); // mengabil semua li
const a = document.querySelector('a'); // mengambil elemen a berupa href

for(var i = 0; i<div.length ; i++) {
    div[i].style.backgroundColor = 'Red' // ubah warna merah
}; // perulangan untuk setiap div agar berwarna merah

a.setAttribute("href", "https://teknohole.com/") // mengubah href # menjadi link untuk google bisa https://google.com/

for(var i = 0; i<li.length ; i++) {
    li[i].style.backgroundColor = 'Blue'; // mengubah bakground menjadi biru
    li[i].style.fontSize = '40px'; // mengubah ukuran text menjadi 40px
    li[i].style.fontStyle = 'Arial'; // mengubah style menjadi arial
    li[i].innerHTML = 'Arbath Abdurrahman'; // mengubah text list menjadi nama saya
};
