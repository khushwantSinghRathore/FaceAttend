<?php
session_start();
//$sem = $_SESSION['sem'];
$con = mysqli_connect('localhost','root','','khush');
$limit = 2;
	if(isset($_GET['page'])){
		$page = $_GET['page'];
	}
	else{

		$page = 1;
		}
	$st = ($page -1 )*$limit;	$result = mysqli_query($con,"select * from info order by rollnum asc limit $st,$limit");
		/* (isset($_POST['next'])){
		$cp = $_SESSION['cp'];
		$a = $_POST["a"];
		if ($a < $cp) {
			$a = $_POST["a"]+1;
		}
	}

	if(isset($_POST['pre'])){
		if ($_POST["a"]>1) {
			$a = $_POST['a']-1;
		}
	}

	if(!isset($a)){
		$a=0;
	}

	if(isset($_POST['first'])){
		$a=0;
	}

	if(isset($_POST['last'])){
		$a = $_SESSION['cp'];
	}
	*/
	
	//$cp = $row;
	//$_SESSION['cp'] = $row;
	//$result = mysqli_query($con,"select * from info where semester = '".$sem."' Offset ".$a." ");
	//if($cp >0){
			echo "<form method='post' action=''>"; 
			echo "<table> <tr>
			<td> roll number </td>
			<td> name </td>
			<td> semester </td>
			</tr>";

			while($row = mysqli_fetch_assoc($result)){
				echo " <tr>
				<td> $row[rollnum] </td>
				<td> $row[name] </td>
				<td> $row[semester] </td>
				</tr>
				";
			}
				echo "</table>";
				$rs = mysqli_query($con,"select count(rollnum) as total from info ");
				$row = mysqli_fetch_array($rs);
				$total = $row[0];
				$totalpage = ceil($total/$limit);
				
				for($i=1;$i <= $totalpage;$i++) { 
					echo "<a href='real.php?page=".$i."'>".$i."</a>";
				}
				//echo $pageLink. "<div>";
				//echo "<input type='hidden' name='a' value='$a'>";
				//echo "<input type='submit' name='next' value='next'>";
				//echo "<input type='submit' name='first' value='first'>";
				//echo "<input type='submit' name='pre' value='pre'>";
				//echo "<input type='submit' name='last' value='last'>";
				echo "</form>";
	//}
?>