<?php
if(isset($_POST['submit'])) {
$conn = new mysqli("localhost", "root", "", "result");
$sql="select * from admin where sid = '".$_POST['sid']."' and dob = '".$_POST['dob']."'";
$conn->query($sql);
$result = $conn->query($sql);
	if($result->num_rows == 1){
		while($row = $result->fetch_assoc()) {
			if($result->num_rows > 0){
				echo "<table align='center'> <tr> ";
				echo " <td> Name :".$row["sname"]." </td> ";
				echo "<td> Roll Number :".$row["sid"]." </td> </tr>";
				echo "<tr> <td> Father Name :".$row["fname"]." </td> ";
				echo "<td> Mother Name :".$row["mname"]." </td> </tr>";
				echo "<tr> <td> Email :".$row["email"]." </td> ";
				echo "<td> Contact :".$row["scontact"]." </td> </tr> </table>";
				echo "<center> Semester :".$row["course"]." </center> ";
				$trnm = $row["result"];
			}
		}
	$totalInt = 0;
	$totalExt = 0;
	$maxInt = 20;
	$maxExt = 80;
	$cout = 0;
	$sql="select * from $trnm";
	$conn->query($sql);
	$result = $conn->query($sql);
	echo "<table boarder = 1 align='center'>";
	while($row = $result->fetch_assoc()) {
		if ($result->num_rows > 0){
			$cout = $cout + 1;
			echo "<tr>	";
			echo "<td> ".$row["papercode"]." </td> <td> ".$row["papername"]." </td>  <td> $maxInt </td>  <td> ".$row["internals"]." </td> <td> $maxExt </td> <td> ".$row["externals"]."</td> ";
			$totalInt = $totalInt +	$row["internals"];
			$totalExt = $totalExt +	$row["externals"];
			echo "</tr>";
		}
	}
	$maxInt = $maxInt * $cout;
	$maxExt = $maxExt * $cout;
	echo "<tr> <td> Total </td> <td>  </td> <td> $maxInt <td> $totalInt </td> <td> $maxExt </td> <td> $totalExt </td> </tr>";
	echo "</table>";
	$outof = $maxInt + $maxExt;
	$grandtotal = $totalInt + $totalExt;
	$percent = $grandtotal / $outof * 100 ;
	if($percent > 33){
	echo "<center> Maximumtotal : $outof     Grandtotal : $grandtotal  </br>    Percentage : $percent      Result : Pass </center>";
	}
	else{
		echo "<center> Maximumtotal : $outof     Grandtotal : $grandtotal  </br>    Percentage  : $percent     Result : Failed </center>";
	}
	$conn->close();
	}
	else{
		header("location: maresult.php");
	}
}
else{	
?>
<html>
<body>
	<form name="form1" action="" method="post">
	<B>
		<center>
	<h1> Result </h1>
	<table border=1 align=center>
			<tr>
			<td>Student Id:</td>
			<td><input type="number" name="sid"  required > </input> </td>
			</tr>
			<tr>
			<td>Date Of Birth:</td>
			<td><input type="date" name="dob" required> </input> </td>
			</tr>
	</table>
	<button type="submit" name="submit"> Click Here</button>	
	</center>
	</B>
	</form>	
</body>
</html>
<?php
}
?>