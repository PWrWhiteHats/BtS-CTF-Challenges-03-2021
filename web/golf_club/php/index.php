<?php
#if(!is_writable(session_save_path())){
#    echo 'Session path "'.session_save_path().'" is not writable for PHP!'; 
#    phpinfo();
#}
?>
<!DOCTYPE HTML>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Golf player`s leaderboard</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-sm-10">
                    <h1 class="text-center">Golf player`s leaderboard</h1>
                    <table class="table mt-5">
                        <thread>
                            <tr>
                                <th scope="col">No.</th>
                                <th scope="col">Name</th>
                                <th scope="col">Surname</th>
                                <th scope="col">Club name</th>
                                <th scope="col">R1</th>
                                <th scope="col">R2</th>
                                <th scope="col">Sum</th>
                                <th scope="col">Profile</th>
                            </tr>
                        </thread>
                        <tbody>
<?php

$mysql_conn = new mysqli('127.0.0.1','devuser','devpass','test_db');

if($mysql_conn->connect_error){
    die("Connection falied:".$mysql_conn->error.". Please contact administrator");
}

#$mysql_conn->query("insert into leaderboard values(73,'Szymon','Dabrowski','Warszawa golf club',35,22,0,'Enter your description here...')");

$sql_query = "SELECT *, r1+r2 as total FROM leaderboard ORDER BY total DESC";
$result = $mysql_conn->query($sql_query);

if($result->num_rows){
    $iterator=1;
    while($row=$result->fetch_assoc()){
        $name="n/a";
        $surname = "-"; 
        $club_name = "-";
        $href='';
        if($row['visible']==1)
        {
           $name = $row['name'];
           $surname = $row['surname']; 
           $club_name = $row['club_name'];
           $href='<a href="/player.php?id='.$row['id'].'">Profile</a>';
        }
        echo ' 
                    <tr>
                        <th scope="row">'.$iterator.'</th>
                        <td>'.$name.'</td>
                        <td>'.$surname.'</td>
                        <td>'.$club_name.'</td>
                        <td>'.$row['r1'].'</td>
                        <td>'.$row['r2'].'</td>
                        <td>'.$row['total'].'</td>
                        <td>'.$href.'</td>
                        </th>
                    </tr>
            ';
    
    $iterator++;
    }
}

$mysql_conn->close();

?>
                        <tbody>
                    </table>
                </div>
            </div>
        </div>
    </body>
</html>
