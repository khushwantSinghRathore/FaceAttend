<?php
if(isset($_POST['go'])){
	session_start();
		$_SESSION['sem'] = $_POST['sem'];
		header("location:real.php");

}else{
?>
<!DOCTYPE html>
<html>

<body>
<form action="" method="post">
<select name="sem">
	<?php
	$con = mysqli_connect('localhost','root','','khush');
	$rs = mysqli_query($con, "select distinct semester from info");
	while($row = mysqli_fetch_array($rs)){
		echo "<option value = '".$row[0]."'>".$row[0]."</option>";
	}
	?>
</select>
<input type="submit" name="go">
</form>
</body>
</html>
<?php
}
?>