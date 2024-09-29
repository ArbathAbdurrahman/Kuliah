<?php
include 'koneksi.php';
include 'navbar.php';
?>

<h3> <center>Input Data Mahasiswa</center>  </h3>
<div class="container">
<a class = "btn btn-primary" href="index.php"> Data Mahasiswa </a>
<form action = "" method="POST">
    <div class="form-group">
      <label for="nim">NIM</label>
      <input type="text" name="nim" class="form-control"  placeholder="Masukan NIM" required>
    <div class="form-group">
  <div class="form-group">
    <label for="nama">Nama Lengkap</label>
    <input type="text" name="nama" class="form-control"  placeholder="Masukan Nama Lengkap" required>
  <div class="form-group">
    <label for="prodi">Prodi</label>
    <input type="text" name="prodi" class="form-control"  placeholder="Masukan Prodi" required>
  <div class="form-group">
    <label for="asal">Asal</label>
    <input type="text" name="asal" class="form-control"  placeholder="Masukan Asal" required>
    <br>
    <td><input class="btn btn-success" type="submit" name="simpan" value="simpan"></td>
    </div>
  <?php
    include 'koneksi.php';
    if (isset($_POST['simpan'])){
    $insert = mysqli_query($conn, "INSERT INTO tb_mahasiswa VALUES 
                ('".$_POST['nim']."',
                '".$_POST['nama']."',
                '".$_POST['prodi']."',
                '".$_POST['asal']."')");
        if ($insert){
            echo "berhasil disimpan";
        } else {
            echo "gagal disimpan";
        }
    }
    ?>
</form>