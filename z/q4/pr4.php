<?php
session_start();
	switch(true){
    case isset($_POST['std']):
		$roll = $_POST['stdid'];
		$papercode = array( );
		$paper = array( );
	 	$conn = new mysqli("localhost", "root","", "result");
		$sql = "select * from admin where sid = $roll";
		$result = $conn->query($sql);
		if($result->num_rows == 1){
			while($row = $result->fetch_array()){
				if ($result->num_rows > 0){
					$roll = $row[0];
					$nam = $row[1];
					$sem = $row[10];  
					$email = $row[7];
					$contact = $row[8];
				}
			}
		}
		$sql1 = "select * from $sem";	
		$res = $conn->query($sql1);
		if($res->num_rows > 0){
			while($row = $res->fetch_assoc()){
				if ($res->num_rows > 0){ 
					$papercode[] = $row['code'];
					$paper[] = $row['subject'];
				}
			}
		}
		$_SESSION['papercode'] = $papercode;
		$_SESSION['paper'] = $paper;
		break;
case isset($_POST['submit']):
			$r="result";
			$roll = $_POST['inp2'];
			$_SESSION['rnm'] = $roll;
			$tab = $r.$roll ;
			$_SESSION['rec'] = $tab;
			$internals = array( $_POST['sb1'],$_POST['sb2'],$_POST['sb3'],$_POST['sb4'],$_POST['sb5'],$_POST['pr1'],$_POST['pr2']);
			$externals = array( $_POST['sb11'],$_POST['sb22'],$_POST['sb33'],$_POST['sb44'],$_POST['sb55'],$_POST['pr11'],$_POST['pr22']);
			$conn = new mysqli("localhost", "root", "", "result");
			$sql = "create table $tab(papercode varchar(10),papername varchar(20),internals int(5),externals int(5))";
			$conn->query($sql);
			$sql ="UPDATE admin SET result = '".$tab."' WHERE sid = $roll";
			$conn->query($sql);
			$arr = $_SESSION['papercode'];
			$arr2 = $_SESSION['paper'];
				for ($i=0; $i < 7 ; $i++) { 
				$sql = "insert into $tab value('".$arr[$i]."','".$arr2[$i]."',$internals[$i],$externals[$i])";
				$conn->query($sql);
				}
			header('location:pr41.php');
			$conn->close();
		break;
	}
if(isset($_POST['std'])){		
?>
<html>
	<body>
	<form name="form" action="" method="post"><B><center>
			<table border=1 align=center>
			<tr><td>Name:</td>
				<td>Roll Number</td>
				<td>Semester</td>
				<td>Email:</td>
				<td>Contact:</td>
			</tr>
			<tr>
			<td><input type="text" name="inp1" required  value='<?php echo $nam ?>'  > </input> </td>
			<td><input type="text" name="inp2" required  value='<?php echo $roll ?>'  > </input> </td>
			<td><input type="text" name="inp3" required  value='<?php echo $sem ?>'  > </input> </td>
			<td><input type="email" name="inp4"required  value='<?php echo $email ?>'   > </input></td>
			<td><input type="text" name="inp5" required  value='<?php echo $contact ?>'  > </input></td>
			</td>
			</table>
			</br>
			</br>
			</br>
			<table border="0" align="center">
			<tr>
				<th> Paper Code </th>
				<th> Paper Name </th>
				<th> Internals MAX(20) </th>
				<th> Externals MAX(80) </th>
			</tr>	
			<tr>
			<td> <?php echo $papercode[0] ?></label></td>
			<td> <?php echo $paper[0] ?></td>
			<td><input type="text" name="sb1"  required > </input> </td>
			<td><input type="text" name="sb11"  required > </input> </td>
			</tr>

			<tr>
			<td> <?php echo $papercode[1] ?></td>
			<td> <?php echo $paper[1] ?></td>
			<td><input type="text" name="sb2"  required > </input> </td>
			<td><input type="text" name="sb22"  required > </input> </td>
			</tr>
			<tr>
			<td> <?php echo $papercode[2] ?></td>
			<td> <?php echo $paper[2] ?></td>
			<td><input type="text" name="sb3"  required > </input> </td>
			<td><input type="text" name="sb33"  required > </input> </td>
			</tr>
			<tr>
			<td> <?php echo $papercode[3] ?></td>
			<td> <?php echo $paper[3] ?></td>
			<td><input type="text" name="sb4"  required > </input> </td>
			<td><input type="text" name="sb44"  required > </input> </td>
			</tr>
			<tr>
			<td> <?php echo $papercode[4] ?></td>
			<td> <?php echo $paper[4] ?></td>
			<td><input type="text" name="sb5"  required > </input> </td>
			<td><input type="text" name="sb55"  required > </input> </td>
			</tr>
			<tr>
			<td> <?php echo $papercode[5] ?></td>
			<td> <?php echo $paper[5] ?></td>	
			<td><input type="text" name="pr1"  required > </input> </td>
			<td><input type="text" name="pr11"  required > </input> </td>
			</tr>
			<tr>
			<td> <?php echo $papercode[6] ?></td>
			<td> <?php echo $paper[6] ?></td>
			<td><input type="text" name="pr2"  required > </input> </td>
			<td><input type="text" name="pr22"  required > </input> </td>
			</tr>
			</table>
		<br><br>
		<input type="submit" name="submit"> </input>
		</center>
		</B>
	</form>
	</body>
</html>
<?php 
}
else{
?>	
<html>
	<body>
	<form name="form1" action="" method="post">
	<B>
		<center>
			<h1> Regestration form for Result </h1>
			<br><br>
			<h3> Enter Student Id :</h3>
			<input type="text" name="stdid"  required> </input>
			<input type="submit" name="std" value="check"> </input>
		</center>
	</B>
	</form>
	</body>
</html>
<?php 
}
?>










