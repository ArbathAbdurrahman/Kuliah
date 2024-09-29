<?php
include 'koneksi.php';
if (isset($_GET['kode_mk'])){
    $delete = mysqli_query($conn, "DELETE FROM tb_mk WHERE kode_mk = '".$_GET['kode_mk']."' ");
    header ('location:mata-kuliah.php');
}

?> 