// Tugas 1
const ubahWarna = document.getElementById('ubahWarna');
const warnaParagraf = document.getElementById('warnaParagraf');

ubahWarna.addEventListener('click', () => {
    if (warnaParagraf.style.color === 'blue'){
        warnaParagraf.style.color = 'orange';
    }else {
        warnaParagraf.style.color = 'blue';
    }
});

// Tugas 2
const hoverMouse = document.getElementById('hoverMouse');
const pesan = document.getElementById('pesan');

hoverMouse.addEventListener('mouseover', () => {
    pesan.textContent = 'Kunjungi Teknohole.com';
});

hoverMouse.addEventListener('mouseout', () => {
    pesan.textContent = '';
});

// Tugas 3
const kata = document.getElementById('kata');
const kataTerakhir = document.getElementById('kataTerakhir');

kata.addEventListener('keydown', (event) => {
    kataTerakhir.textContent = `Huruf Terakhir: ${event.key}`;
});

// Tugas 4
const listInput = document.getElementById('listInput');
const addItemButton = document.getElementById('addItemButton');
const dynamicList = document.getElementById('dynamicList');

addItemButton.addEventListener('click', () => {
    const newItemText = listInput.value.trim();
    if (newItemText) {
        const newListItem = document.createElement('li');
        newListItem.textContent = newItemText;
        dynamicList.appendChild(newListItem);
        listInput.value = ''; // Membersihkan input
    }
});
