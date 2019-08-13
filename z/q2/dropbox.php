<?php
if(isset($_POST["sub"])){
	if(isset($_POST["cors"])){
	$cor=$_POST['cors'];
	$conn = new mysqli("localhost", "root", "", "mlsu");
	$sql =("select * from $cor");
	$result = $conn->query($sql);
	echo "<center> <table border = '1' align = 'center'>";
	echo "Syllabus of $cor </br> </br>";
		if($result->num_rows > 0){
			while($row = $result->fetch_assoc()){
			echo "<tr> <td> ".$row['papercode']." </td> <td> ".$row['papername']." </td> <td> ".$row['teachername']." </td> </tr>";
			}
		}
		echo "</table> </center>";
		$conn->close();
		}
	}else{ ?>
<html>
<body>
<form name="form" method="post"> <center>
<B> <h1> Choose The Semester </h1>
<select name="cors">
  <option value="mca1">Mca 1</option>
  <option value="mca2">Mca 2</option>
</select> <br> <br>
<input type="submit" name="sub" value="syllabus"> </input>
</B> </center> </form>
</body>
</html>
<?php } ?>