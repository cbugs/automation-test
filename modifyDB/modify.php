<?php
$found=false;
$testCaseName= filter_input(INPUT_POST,'testCaseName');
$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "testcasedb";


// Connection for testCases DB
$conn = new mysqli ($host, $dbusername, $dbpassword, $dbname);
$array;

if(!empty($_POST['testCaseName'])){

    $query = "SELECT * FROM  testcases
    WHERE testCaseName='$testCaseName'";

    $results=mysqli_query($conn,$query);
    $array=mysqli_fetch_all($results,MYSQLI_ASSOC);
    mysqli_free_result($results);
    mysqli_close($conn);
    $found=true;
  }

?>

<!DOCTYPE html>
<html>
<center><div class="container">
    <h1>Test Case Modifier</h1>
<div>
    <style>
        .textbox{
            width:250px;
            border-radius:5px;
            font-family:Century Gothic;   
        }
        .container{
            border-radius: 20px;
            background-color: aliceblue;
            height: 500px;
            width: 900px;
        }
    </style>
<form action="modify.php" method="POST">
    Test Case Name: <input type="text" class="textbox" name="testCaseName">
    <input type="submit" value="search">
    <table>
            <tr>
                <th>Command</th>
                <th>Target</th> 
                <th>Value</th> 
            </tr>
        <?php if($found){ ?>
        <?php foreach($array as $row): ?>
            <tr>
                <td>
                    <input type="text" id="<?php echo 'command'.$row["ID"];?>" name="command" class="textbox" value="<?php echo $row["command"];?>">
                </td>
                <td>
                    <input type="text" id="<?php echo 'target'.$row["ID"];?>" name="target" class="textbox" value="<?php echo $row["target"];?>">
                </td>
                
                <td>
                    <input type="text" id="<?php echo 'value'.$row["ID"];?>" name="value" class="textbox" value="<?php echo $row["value"];?>">

                </td>
                 <td>
                    <input type="button" id="<?php echo $row["ID"];?>" value="SAVE" name="Save" onclick="addToDB(this.id)">

                </td>
            </tr>
        <?php endforeach; ?>
        
        <?php } ?>
    </table>
</form>
</div>
</div></center>

<script>
    function addToDB(value){
        console.log(value)
    var myAjax= new XMLHttpRequest();
    myAjax.open("POST","update.php",true);
    myAjax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var command=document.getElementById("command"+value).value;

    var target=document.getElementById("target"+value).value;
    var val=document.getElementById("value"+value).value;
    
    myAjax.onreadystatechange= function(){
        if(myAjax.readyState==4 && myAjax.status==200){
            // alert(command + target + val);
            // alert("Update successful");
        }

        else{
            // alert("Update failed");
        }
    };
    
    myAjax.send("Save="+value+"& command="+command+"& target="+target+"& value="+val);
}



</script>
</html>
