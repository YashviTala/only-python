<form action="" method="POST">
   
	<input type="text" name="" placeholder="Enter " >
    <input type="text" name="" placeholder="Enter " >
    <input type="text" name="" placeholder="Enter " >
    <input type="submit" name="submit" value="">
</form>

<?php
$con = mysqli_connect("localhost", "root", "", "");

if (!$con) {
    die("Connection failed: " . mysqli_connect_error());
}

if (isset($_POST[''])) {
	$ = $_POST[''];
    $ = $_POST[''];
    $ = $_POST[''];
    
    
    $qry = "INSERT INTO (,, ) VALUES('$','$' ,'$')";

    if (mysqli_query($con, $qry)) {
        echo "Data inserted successfully!";
      
    } else {
        echo "Error: " . mysqli_error($con);
    }
}
?>
