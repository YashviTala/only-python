<table border="1">
    <tr>
        <th>id</th>
        <th>name</th>
        <th>city</th>
    </tr>

<?php
$con=mysqli_connect("localhost","root","","university");
if(!$con)
{
    exit();
}

$qry="select * from student";
$result=mysqli_query($con,$qry);
//print_r($result);

if(mysqli_num_rows($result)>0)
{
    while($row=mysqli_fetch_assoc($result))
    {
        echo "<tr>";
        echo "<td>" . $row['id'] . "</td>";
        echo "<td>" . $row['name'] . "</td>";
        echo "<td>" . $row['city'] . "</td>";
        echo "<td>";
        echo "<a href='fdelete.php?id=" . $row['id'] . "'>delete</a>";
        echo "</td>";
        echo "<td>";
        echo "<a href='fupdate.php?id=" . $row['id'] . "'>update</a>";
        echo "</td>";
        echo "</tr>";
    }
}
echo "</table>";

?>