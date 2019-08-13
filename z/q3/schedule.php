<?php
session_start();
if(isset($_POST['sub1']))
{
	$st=$_POST["time1"]; $inv=$_POST["time2"]; $et=$_POST["time3"]; $pt=$_POST["time4"]; 
	$db=$_SESSION['cor']; $last=$st; $j=0;
	$t1=$_POST['t1']; $t2=$_POST['t2']; $t3=$_POST['t3']; $t4=$_POST['t4']; $t5=$_POST['t5'];
	$sub = array($_SESSION['s1'],$_SESSION['s2'],$_SESSION['s3'],$_SESSION['s4'],$_SESSION['s5']);
	$tall = array($t1,$t2,$t3,$t4,$t5);
	$conn = new mysqli("localhost", "root", "", "college");
	$sql ="create table $db(time float(10,2),subject varchar(20),teacher varchar(30))";
	$conn->query($sql);
	for($i=$st;$i<$inv;$i=$i + $pt){
		$sql ="insert into $db values($i,'$sub[$j]','$tall[$j]')";
		$conn->query($sql);
		$j=$j+1;
	}
	$sql ="insert into $db values($i,'intervel','-')";
	$conn->query($sql);
	for($i=$inv+.30;$i<$et;$i=$i + $pt){
		$sql ="insert into $db values($i,'$sub[$j]','$tall[$j]')";
		$conn->query($sql);
		$j=$j+1;
	}
	mysqli_commit($conn);
	header("location:finalout.php");
}else{
?>
<html>
<body>
<center>
<form name='f2' action="" method="POST">
<h1> Enter the details for the Time Table </h1>
<input type="text" name="time1" placeholder="Start time" required="">
<input type="text" name="time2" placeholder="intervel time" required="">
<input type="text" name="time3" placeholder="end time" required="">
<input  type="text" name="time4" placeholder="each period time" required="">	
</br></br></br>	
<table align="center">
<tr> <td> <?php echo $_SESSION['s1']; ?> </td>
<td> <input   type="text" name="t1" placeholder="teacher name" required=""> </td> </tr>	
<tr> <td> <?php echo $_SESSION['s2']; ?> </td> 
<td> <input type="text" name="t2" placeholder="teacher name" required=""> </td> </tr>	
<tr> <td> <?php echo $_SESSION['s3']; ?> </td>
<td> <input type="text" name="t3" placeholder="teacher name" required=""> </td> </tr>	
<tr> <td> <?php echo $_SESSION['s4']; ?> </td>
<td> <input  type="text" name="t4" placeholder="teacher name" required=""> </td> </tr>	
<tr> <td> <?php echo $_SESSION['s5']; ?> </td>	
<td> <input  type="text" name="t5" placeholder="teacher name" required=""> </td> </tr>	
</table>
</br></br>
<button type="submit" name="sub1"> Go </button>
</form>	
</center>
</body>
</html>
<?php } ?>