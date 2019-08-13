<?php
session_start();
if(session_status() != PHP_SESSION_NONE){
$com=$_SESSION['studid']; }
	if(isset($_POST['submit'])){
		$conn = new mysqli("localhost", "root", "", "result");
		$sql="select sid from admin where sid='" .$_POST['sid']. "'";
		$result = $conn->query($sql);
		if($result->num_rows > 0){
			echo "<script> alert('Student id Exists');
			window.history.back(); </script>";
		}else{
		$sql ="insert into admin values('" .$_POST['sid']. "','" .$_POST['sn']. "','" .$_POST['fn']. "','" .$_POST['mn']. "','" .$_POST['adds']. "','" .$_POST['gender']. "','" .$_POST['dob']. "','" .$_POST['em']. "','" .$_POST['scn']. "','" .$_POST['pcn']. "','" .$_POST['cor']. "')";
		$conn->query($sql);
		$sql="insert into user values('" .$_POST['sid']. "','" .$_POST['dob']. "')";
		$conn->query($sql);
		$sql="select id from employee where id='" .$com. "'";
		$result = $conn->query($sql);
		if($result->num_rows == 1){
		header("location:dash.php");
		}else{
		header("location:studentlogin.php");
		}}
	}else{ ?>	
<html>
	<body>
	<form name="form1" action="" method="post"> <B> <center>
		<h1> Admission Form </h1> <br> <br>
			<table border=1 align=center>
			<tr><td>Student Name:</td>
				<td><input type="text" name="sn"  > </input> </td>
			</tr>
			<tr><td>Father Name:</td>
				<td><input type="text" name="fn" > </input> </td>
			</tr>
			<tr><td>Mother Name:</td>
				<td><input type="text" name="mn" > </input> </td>
			</tr>
			<tr><td>Address:</td>
				<td><input type="text" name="adds" > </input> </td>
			</tr>
			<tr><td>Gender:</td>
				<td><input type="radio" name="gender" value="male" checked> Male
					<input type="radio" name="gender" value="female"> Female </td>
			</tr>
			<tr><td>Date of birth:</td>
				<td><input type="date" name="dob" > </input> </td>
			</tr>
			<tr><td>Email:</td>
				<td><input type="email" name="em" > </input></td>
			</tr>
			<tr><td>Student Contact:</td>
				<td><input type="number" name="scn" > </input></td>
			</tr>
			<tr><td>Parents Contact:</td>
				<td><input type="number" name="pcn" > </input></td>
			</tr>
			<tr><td>Course:</td>
				<td> <select name="cor">
  					 <option value="MCA">MCA</option>
  					 <option value="BCA">BCA</option>
					</select></td>
			</tr>
			<tr><td>Student ID:</td>
				<td> <input type='number' name='sid'  required=""> </input></td>
			</tr>
		</table> </br> </br> </br>
		<button type="submit" name="submit">conform</button>  
		</center> </B> </form>
	</body>
</html>
<?php } ?>