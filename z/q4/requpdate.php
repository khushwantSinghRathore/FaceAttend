<?php
session_start();
$sid=$_SESSION['studid'];
if(isset($_POST['submit'])){
	$conn = new mysqli("localhost", "root", "", "result");
	$sql="select sid from admin where sid='" .$sid. "'";
	$result = $conn->query($sql);
	if($result->num_rows == 1){
		if(isset($_POST['up1'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update `admin` set `sname` = ''".$_POST["sn"]."'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up2'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set fname = ''".$_POST['fn']."'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up3'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set mname = ''" .$_POST['mn']. "'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up4'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set address = ''" .$_POST['adds']. "'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up5'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set gender = ''" .$_POST['gender']. "'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up6'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set dob = ''" .$_POST['dob']. "'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up7'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set email = ''" .$_POST['em']. "'' where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up8'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin set scontact = " .$_POST['scn']. " where sid = $sid')";
			$conn->query($sql);
		}
		if(isset($_POST['up9'])){
			$sql = "INSERT INTO requp VALUES ('$sid', 'update admin pcontact = " .$_POST['pcn']. " where sid = $sid')";
			$conn->query($sql);
		}
	header("location:dash1.php");
	}
	}
else{
?>
<html>
	<body>
	<form name="form1" action="" method="post">
		<B>
		<center>
		<h1> Update Information </h1>
		<br><br>
			<table border=1 align=center>
			<tr>
			<td><input type="checkbox" name="up1" value="name"></td>
			<td>Student Name:</td>
			<td><input type="text" name="sn"  > </input> </td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up2" value="fname"></td>
			<td>Father Name:</td>
			<td><input type="text" name="fn" > </input> </td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up3" value="fname"></td>
			<td>Mother Name:</td>
			<td><input type="text" name="mn" > </input> </td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up4" value="fname"></td>
			<td>Address:</td>
			<td><input type="text" name="adds" > </input> </td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up5" value="fname"></td>
			<td>Gender:</td>
			<td>
				<input type="radio" name="gender" value="male" checked> Male
				<input type="radio" name="gender" value="female"> Female  
			</td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up6" value="fname"></td>
			<td>Date of birth:</td>
			<td><input type="date" name="dob" > </input> </td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up7" value="fname"></td>
			<td>Email:</td>
			<td><input type="email" name="em" > </input></td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up8" value="fname"></td>
			<td>Student Contact:</td>
			<td><input type="number" name="scn" > </input></td>
			</tr>
			<tr>
			<td><input type="checkbox" name="up9" value="fname"></td>
			<td>Parents Contact:</td>
			<td><input type="number" name="pcn" > </input></td>
			</tr>
			<tr>
		</table>
		</br>
		</br>
		</br>
		<button type="submit" name="submit">conform update</button>  
		</center>
		</B>
	</form>
	</body>
</html>
<?php
}
?>