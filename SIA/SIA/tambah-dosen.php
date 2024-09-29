<?php
include 'koneksi.php';
include 'navbar.php';
?>

<h3> <center>Input Data Mahasiswa</center>  </h3>
<div class="container">
<a class = "btn btn-primary" href="index-dosen.php"> Data Dosen </a>
<form action = "" method="POST">
    <div class="form-group">
      <label for="nim">NID</label>
      <input type="text" name="nid" class="form-control"  placeholder="Masukan NID" required>
    <div class="form-group">
  <div class="form-group">
    <label for="nama">Nama Lengkap</label>
    <input type="text" name="nama_dosen" class="form-control"  placeholder="Masukan Nama Lengkap" required>
  <div class="form-group">
    <label for="prodi">Kode Mata Kuliah</label>
    <input type="text" name="kode_mk" class="form-control"  placeholder="Masukan Kode mata kuliah" required>
  <div class="form-group">
    <label for="asal">Mata Kuliah</label>
    <input type="text" name="mk" class="form-control"  placeholder="Masukan Mata Kuliah" required>
    <br>
    <td><input class="btn btn-success" type="submit" name="simpan" value="simpan"></td>
    </div>
  <?php
    include 'koneksi.php';
    if (isset($_POST['simpan'])){
    $insert = mysqli_query($conn, "INSERT INTO tb_dosen VALUES 
                ('".$_POST['nid']."',
                '".$_POST['nama_dosen']."',
                '".$_POST['kode_mk']."',
                '".$_POST['mk']."')");
        if ($insert){
            echo "berhasil disimpan";
        } else {
            echo "gagal disimpan";
        }
    }
    ?>
</form>