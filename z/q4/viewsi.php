<?php 
session_start();
if(isset($_POST['submit']))
	$con = mysqli_connect("localhost","root","","mlsu");
	$query = "select * from mydb";
	$result = mysqli_query($con,$query);
	while( $row = mysqli_num_rows($result)){
		echo "$row['id']";
		echo "$row['name']";
		echo "$row['place']";
	}
$_SESSION['id'] = $row['id'];


}
session_destroy();
?>