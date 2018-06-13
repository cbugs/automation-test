<?php

header("Cache-Control: no-cache");
header("Content-type: text/plain");

if(isset($_POST['Save'])){
    $id=$_POST['Save'];
    $command=$_POST['command'];
    $target=$_POST['target'];
    $value=$_POST['value'];

    $host = "localhost";
    $dbusername = "root";
    $dbpassword = "";
    $dbname = "testcasedb";

    $conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);
    $target1= addslashes($target);
    $query = "UPDATE testcases 
            SET command='".$command."', target='".$target1."', value='".$value."'
            WHERE ID='".$id."'";

    $results=mysqli_query($conn,$query);

    var_dump($conn->error);

    mysqli_close($conn);
 
}else{
     echo "wrong";
 }


?>