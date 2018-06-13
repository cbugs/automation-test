<?php
sleep(3);
$output = '';

$file = "xmlkatalon.xml";

if(isset($_FILES['file']['name']) &&  $_FILES['file']['name'] != '')
{
 
    $valid_extension = array('xml');
 $file_data = explode('.', $_FILES['file']['name']);
 $file_extension = end($file_data);
 
 if(in_array($file_extension, $valid_extension))
 {
    $xml = simplexml_load_file($_FILES['file']['tmp_name']);
    //$xml=simplexml_load_file($file) or die("Error: Cannot create object");

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "testcasedb";

    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection

    if ($conn->connect_error) 
    {
        die("Connection failed: " . $conn->connect_error);
    }

    foreach ($xml->children() as $row) 
    {
        $command = $row->command;
        $target = $row->target;
        $value = $row->value;
        $target1 = addslashes($target);

        $sql = "INSERT INTO testCase (testCaseName, dateCreated, command, target,value )
        VALUES ('".$file."','".date("Y-m-d H:i:s", time())."','".$command."', '".$target1."', '".$value."')";

            if ($conn->query($sql) === TRUE) 
            {
                echo "New testcase record created successfully";
            } 
            else 
            {
                echo "Error: " . $sql . "<br>" . $conn->error;
            }
    }

$conn->close();
 }
}
?>