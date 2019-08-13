<?php
session_start();
if(isset($_POST['s1'])){
	$_SESSION['cor']=$_POST["cor"];
	$_SESSION['s1']=$_POST["sub1"];
	$_SESSION['s2']=$_POST["sub2"];
	$_SESSION['s3']=$_POST["sub3"];
	$_SESSION['s4']=$_POST["sub4"];
	$_SESSION['s5']=$_POST["sub5"];
	$cor=$_SESSION['cor'];
$conn = new mysqli("localhost", "root", "", "college");
$sql1 = "DESCRIBE `$cor`";
$val = $conn->query($sql1);
if($val) {
     echo "DO SOMETHING! IT EXISTS!";
     sleep(2);
     header("location:timetable.php");
}
$sql ="insert into timetab() values('".$_SESSION['s1']."','".$_SESSION['s2']."','".$_SESSION['s3']."','".$_SESSION['s4']."','".$_SESSION['s5']."','".$_SESSION['cor']."')";
$conn->query($sql);
echo "you have entered into database";
header("location:schedule.php");
$conn->close();
}
else{
?>
<html>
<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>
<body>
<center>
	<h1> Enter the subjects Name </h1>
</br></br></br>
<form name='f1' action="" method="POST">
<div class="container">
	<div class="form-group">
		<div class="row">
    <div class="col-sm-4">
<input class="form-control" type="text" name="cor" placeholder="course name" required="">
</br>
</br>	
<input class="form-control" type="text" name="sub1" placeholder="Subject name" required="">
</br>
<input class="form-control" type="text" name="sub2" placeholder="Subject name" required="">
</br>

<input class="form-control" type="text" name="sub3" placeholder="Subject name" required="">
</br>

<input class="form-control" type="text" name="sub4" placeholder="Subject name" required="">
</br>

<input class="form-control" type="text" name="sub5" placeholder="Subject name" required="">
</br>
</br>
<button class="btn" type="submit" name="s1">Lets go</button>
</div>
</div>
</div>
</div>
</form>
</center>
</body>
</html>
<?php
}
?>