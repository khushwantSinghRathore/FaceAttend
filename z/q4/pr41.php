<?php
session_start();
$tnm=$_SESSION['rnm'];
$trnm=$_SESSION['rec'];
$conn = new mysqli("localhost", "root", "", "result");
$sql="select * from admin where sid = $tnm";
$conn->query($sql);
$result = $conn->query($sql);
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
		}
	}
	$totalInt = 0; $totalExt = 0; $maxInt = 20; $maxExt = 80; $cout = 0;
	$sql="select * from $trnm";
	$conn->query($sql);
	$result = $conn->query($sql);
	echo "<table align='center'>";
	while($row = $result->fetch_assoc()) {
		if ($result->num_rows > 0){
			echo " <tr> <td> ".$row["papercode"]." </td> <td> ".$row["papername"]." </td>  <td> $maxInt </td>  <td> ".$row["internals"]." </td> <td> $maxExt </td> <td> ".$row["externals"]."</td> </tr>";
			$totalInt = $totalInt +	$row["internals"]; $totalExt = $totalExt +	$row["externals"]; $cout = $cout + 1;
		}
	}
	$maxInt = $maxInt * $cout; $maxExt = $maxExt * $cout;
	echo "<tr> <td> Total </td> <td>  </td> <td> $maxInt <td> $totalInt </td> <td> $maxExt </td> <td> $totalExt </td> </tr>";
	echo "</table>";
	$outof = $maxInt + $maxExt; $grandtotal = $totalInt + $totalExt; $percent = $grandtotal / $outof * 100 ;
	if($percent > 33){
	echo "<center> Maximumtotal : $outof     Grandtotal : $grandtotal  </br>    Percentage : $percent      Result : Pass </center>";
	}
	else{
		echo "<center> Maximumtotal : $outof     Grandtotal : $grandtotal  </br>    Percentage  : $percent     Result : Failed </center>";
	}
	$conn->close();
?>