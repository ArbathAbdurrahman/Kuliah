<?php
include 'koneksi.php';
include 'navbar.php';
?>

<h3> <center>Input Data Mahasiswa</center>  </h3>
<div class="container">
<a class = "btn btn-primary" href="mata-kuliah.php"> Data Mata Kuliah </a>
<form action = "" method="POST">
    <div class="form-group">
      <label for="nama">Kode Mata Kuliah</label>
      <input type="text" name="kode_mk" class="form-control"  placeholder="Masukan Kode Mata Kuliah" required>
    <div class="form-group">
      <label for="nim">Nama Mata Kuliah</label>
      <input type="text" name="nama_matakuliah" class="form-control"  placeholder="Masukan Nama Mata Kuliah" required>
    <div class="form-group">
      <label for="nim">Ruang Kuliah</label>
      <input type="text" name="ruang-kuliah" class="form-control"  placeholder="Masukan Ruang Kuliah" required>
    <div class="form-group">
      <label for="nim">Jadwal Kuliah</label>
      <input type="text" name="jadwal-kuliah" class="form-control"  placeholder="Masukan Jadwal Kuliah" required>
    <br>
    <td><input class="btn btn-success" type="submit" name="simpan" value="simpan"></td>
    </div>
  <?php
    include 'koneksi.php';
    if (isset($_POST['simpan'])){
    $insert = mysqli_query($conn, "INSERT INTO tb_mk VALUES 
                ('".$_POST['kode_mk']."',
                '".$_POST['nama_matakuliah']."',
                '".$_POST['ruang-kuliah']."',
                '".$_POST['jadwal-kuliah']."')");
        if ($insert){
            echo 'berhasil disimpan';
        } else {
            echo 'gagal disimpan';
        }
    }
    ?>
</form>