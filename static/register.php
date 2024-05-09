<?php
require_once('db.php');
$nick = $_POST['Name'];
$phone = $_POST['PhoneNumber'];
$class = $_POST['Class'];
$subj = $_POST['Subjects']; 

$sql = "INSERT INTO `users` (Name,PhoneNumber,Class,Subjects) VALUES ('$nick', '$phone', '$class', '$subj')";
$conn -> query($sql);
 ?>