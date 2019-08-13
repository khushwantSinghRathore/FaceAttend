<?php
session_start();
	if(isset($_POST['b1'])){
	header("location:ad.php");}
	if(isset($_POST['b2'])){
	header("location:upd.php");}
	if(isset($_POST['b3'])){
	header("location:maresult.php");}
	if(isset($_POST['b4'])){
	header("location:pr4.php");}
	if(isset($_POST['logout'])){
	header("location:studentlogin.php");
	session_destroy();}
	if(isset($_POST["ac"])){
	$conn = new mysqli("localhost", "root", "", "result");
	$sql =("select * from requp");
	$result = $conn->query($sql);
	while($row1 = $result->fetch_assoc()){
				if ($result->num_rows > 0){
					$conn = new mysqli("localhost", "root", "", "result");
					$sql1 = $row1['qwery'];
					$conn->query($sql1);
				}
	}
	$sql =("select id from requp ");
	$result = $conn->query($sql);
		while($row = $result->fetch_assoc()){
			if ($result->num_rows > 0){
				$id = $row['id'];
				$sql1="delete from requp where id = '" .$id."'";
				$conn->query($sql1);
			}
		}
	header("location:dash.php");
	}
	if(isset($_POST["dc"])){
		$conn = new mysqli("localhost", "root", "", "result");
		$sql =("select id from requp ");
		$result = $conn->query($sql);
		while($row = $result->fetch_assoc()){
			if ($result->num_rows > 0){
				$id = $row['id'];
				$sql1="delete from requp where id = '" .$id."'";
				$conn->query($sql1);
			}
		}
	header("location:dash.php");
	}else{
?>
<html>
	<body>
	<form name="form" action="" method="post"> <B> <center>
		<h1> COllEGE OF COMPUTER SCIENCE </h1></br></br></br>
			<button type="submit" name="b1">Admission</button> 
			<button type="submit" name="b2">Update</button> 
			<button type="submit" name="b3">Result</button> 
			<button type="submit" name="b4">Result Entry</button>
			</br> </br> </br>
			<button type="submit" name="logout">LogOut</button>
			</br> </br> </br>
			<i> Update Requests </i>
			<?php
			$conn = new mysqli("localhost", "root", "", "result");
			$sql =("select * from requp");
			$result = $conn->query($sql);
			echo "<table>";
			while($row = $result->fetch_assoc()){
						if ($result->num_rows > 0){
						echo "<tr> <td> ".$row["id"]." </td> <td> ".$row["qwery"]."</td> </tr>";	
						}
			}
			echo "</table>";?>
			<button type="submit" name="ac">Accept</button>
			<button type="submit" name="dc">Dicline</button>
		</center> </B>
	</form>	
	</body>
</html>
<?php } ?>