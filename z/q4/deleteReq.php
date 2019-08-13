<?php
session_start();
$sid=$_SESSION['studid'];
if(isset($_POST['Conform'])){
	$conn = new mysqli("localhost", "root", "", "result");
	$sql="select sid from admin where sid='" .$_POST['sid']. "' and dob='" .$_POST['dob']. "'";
	$result = $conn->query($sql);
	if($result->num_rows == 1){
		$sql = "delete from admin where sid = $sid";
		$conn->query($sql);
		header("location:studentlogin.php");
	}
}
else
{
?>
<html>
<body>
	<form name="form1" action="" method="post">
	<B>
		<center>
	<h1> Conform Deletion </h1>
	<table border=1 align=center>
			<tr>
			<td>Student Id:</td>
			<td><input type="text" name="sid"  > </input> </td>
			</tr>
			<tr>
			<td>Date Of Birth:</td>
			<td><input type="date" name="dob" > </input> </td>
			</tr>
	</table>
	</br>
	<button type="submit" name="Conform">Conform</button>	
	</center>
	</B>
	</form>	
</body>
</html>
<?php
}
?>
