<?php
	if(isset($_POST['go'])){
			$rr = mysqli_connect('localhost','root','','khush');
			$rs = mysqli_query($rr,"select * form info group by grandtotal decs");
					echo "<table>
					<tr>
					<td> rollnumber </td>
					<td> name </td>
					<td> semester </td>
					<td> paper-1 </td>
					<td> int </td>
					<td> ext </td>
					<td> paper-2 </td>
					<td> int </td>
					<td> ext </td>
					<td> paper-3 </td>
					<td> int </td>
					<td> ext </td>
					<td> grandtotal </td>
					<td> result </td>
					</tr>";
				while($row = mysqli_fetch_array($rs)){
					echo "<table>
					<tr>
					<td> $row[0] </td>
					<td> $row[1] </td>
					<td> $row[2]</td>
					<td> $row[3]</td>
					<td> $row[4]</td>
					<td> $row[5]</td>
					<td> $row[6]</td>
					<td> $row[7]</td>
					<td> $row[8]</td>
					<td> $row[9]</td>
					<td> $row[10]</td>
					<td> $row[11]</td>
					<td> $row[12]</td>
					<td> $row[13]</td>
					<td> $row[14]</td>
					</tr>";
				}
				echo "</table>";

	}
	else{
?>
<html>
<body>
	<form action="" method="post">
			<select name="sem">
				<?php 
				$con = mysqli_connect('localhost','root','','khush');
				$result = mysqli_query($con,"select distinct semester from info");
				echo "$result";
				while($row = mysqli_fetch_array($result)){
					echo "<option value = '".$row['0']."'>'".$row['0']."'</option>";
				}
				?>
			</select>
			<input type="submit" name="go"> </input>
	</form>
</body>
</html>
<?php
}
?>