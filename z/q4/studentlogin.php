<?php
session_start();
	if(isset($_POST['submit'])){
	$conn = new mysqli("localhost", "root", "", "result");
	$sql="select sid from admin where sid='" .$_POST['sid']. "' and dob='" .$_POST['dob']. "'";
	$result = $conn->query($sql);
	if($result->num_rows == 1){
		$_SESSION['studid']=$_POST['sid'];
		header("location:dash1.php");
	}
	$sql="select id from employee where id='" .$_POST['sid']. "' and dob='" .$_POST['dob']. "'";
	$result = $conn->query($sql);
	if($result->num_rows == 1){
		$_SESSION['studid']=$_POST['sid'];
		header("location:dash.php");
	}}
	if(isset($_POST['sub'])){
		header("location:ad.php");
	}else{ ?>
<html>
<body>
	<form name="form1" action="" method="post"> <B> <center>
	<h1> Login </h1>
	<table border=1 align=center>
		<tr> <td>Student Id:</td>
			 <td><input type="text" name="sid"  > </input> </td>
		</tr>
		<tr> <td>Date Of Birth:</td>
			 <td><input type="date" name="dob" > </input> </td>
		</tr>
	</table> </br>
	<button type="submit" name="submit">For Login Click Here</button>	
	<button type="submit" name="sub">For Addmision Click Here</button>
	</center> </B> </form>	
</body>
</html>
<?php } ?>