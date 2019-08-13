<?php
	if(isset($_POST['b1'])){
	header("location:viewsi.php");
	}
	if(isset($_POST['b2'])){
	header("location:requpdate.php");
	}
	if(isset($_POST['b3'])){
	header("location:maresult.php");
	}
	if(isset($_POST['b4'])){
	header("location:deleteReq.php");
	}
	if(isset($_POST['logout'])){
	header("location:studentlogin.php");
	session_destroy();
	}
	else{
?>
<html>
	<body>
	<form name="form" action="" method="post">
		<B>
			<center>
			<h1> COllEGE OF COMPUTER SCIENCE </h1>
			</br>
			</br>
			</br>
			<button type="submit" name="b1">view records</button> 
			<button type="submit" name="b2">Update request</button> 
			<button type="submit" name="b3">View result</button> 
			<button type="submit" name="b4">Delete request</button>
	</br>
	</br>
	</br>
	<button type="submit" name="logout"> logOut</button>	 
		</center>
		</B>
	</form>
	</body>
</html>
<?php
}
?>