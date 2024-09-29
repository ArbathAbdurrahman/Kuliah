<?php
include 'koneksi.php';
if (isset($_GET['nid'])){
    $delete = mysqli_query($conn, "DELETE FROM tb_dosen WHERE nid = '".$_GET['nid']."' ");
    header ('location:index-dosen.php');
}

?> 