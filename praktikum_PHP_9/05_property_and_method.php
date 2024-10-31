<?php
class Produk {
    public $sku = "001";
    public $merek = "samsung";
    public $harga = 4000000;

    public function pesanProduk(){
        return "Prduk dipesan...";
    }
}
$televisi = new Produk();