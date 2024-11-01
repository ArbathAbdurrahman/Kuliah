<?php

class Produk{
  public $jenis;
  public $merek;

  public function pesanProduk(){
    return $this->jenis." ".$this->merek."dipesan...";
  }
}


$produk01 = new Produk();
$produk01->jenis="Televisi";
$produk01->Merek="Samsung";

$produk02=new Produk();
$produk02->jenis="Mesin Cuci";
$produk02->merek="LG";

echo $produk01->pesanProduk();
echo "<br>";
echo $produk02->pesanProduk();
?>
