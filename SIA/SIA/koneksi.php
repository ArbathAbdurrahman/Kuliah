<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Beranda</title>
</head>

<?php  
$host = "localhost";
$user = "root";
$password = "";
$db = "krs";

$conn = mysqli_connect ($host , $user , $password , $db );
if(!$conn){
    die("koneksi gagal". mysqli_connect_error());
}
?> 