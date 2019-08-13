<?php
session_start();
$tb=$_SESSION['cor'];
$i=0;
$block=0;
$day = array('MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY');
$conn = new mysqli("localhost", "root", "", "college");
	$sql =("select * from $tb");
	$result = $conn->query($sql);
	echo "<div class='table-responsive'>";
	echo "<head>
	<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'> </head>";
	echo "<center> <h1> $tb </h1> <br> <br>";
	echo "<table class='table'>";
		
		echo "<tr>";
		while($block<8){
		if($block==0){
					echo "<td>  </td>";	
				}
		else{		
		while($row = $result->fetch_assoc()){
				if ($result->num_rows > 0){
				echo "<td> ".$row["time"]."</td>";	
				}
				}
		}
		$block=$block+1;
		}
		echo "</tr>";
		while ($i<6) {
		echo "<tr>";
			echo "<th rowspan='2' > $day[$i] </th>";
			$sql =("select * from $tb");
			$result = $conn->query($sql);
			while($row = $result->fetch_assoc()){
				if ($result->num_rows > 0){	
				echo "<td> ".$row["subject"]."</td>";
				}
			}
		echo "</tr>";
		echo "<tr>";	
			$sql =("select * from $tb");
			$result = $conn->query($sql);
			while($row = $result->fetch_assoc()){
				if ($result->num_rows > 0){	
				echo "<td> ".$row["teacher"]."</td>";
				}
			}
		echo "</tr>";
		$i=$i+1;
		}	
	echo "</table>";
	echo "</div>";
	echo "</center>";
	$conn->close();
session_destroy();
?>