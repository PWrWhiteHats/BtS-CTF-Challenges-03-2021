<?php
if(isset($_GET['id'])){
    $header='
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
                        <h1 class="text-center">Golf player`s profile</h1>
                        <div class="card mt-5">
                            <div class="row no-gutters">
                                <div class="col-md-4 bg-secondary"></div>
                                <div class="col-md-8">
                                    <div class="card-body">';

    $mysql_conn = new mysqli('127.0.0.1','devuser','devpass','test_db');

    if($mysql_conn->connect_error){
        die("Connection falied:".$mysql_conn->error.". Please contact administrator");
    }
    
    $id=$mysql_conn->real_escape_string($_GET['id']);

    $sql_query = "SELECT *, r1+r2 as total FROM leaderboard WHERE id=".$id;
    $result = $mysql_conn->query($sql_query);

    if($result->num_rows == 1){
        $rodo_info="";

        while($row=$result->fetch_assoc()){
            if(!$row['visible']){
                if(!isset($_COOKIE['PHPSESSID'])){
                    setcookie('PHPSESSID',md5($id),time()+10800);
                }
                else{
                    if($_COOKIE['PHPSESSID'] == md5($id)){
                        $rodo_info="Private profile";
                    }
                    else{
                        echo $header;
                        echo '<h2 class="card-title">You don`t have access to this private profile</h2>';
                        die();
                    }
                }
            }

            echo $header;

            $total=intval($row['r1'])+intval($row['r2']);

            echo '  <h2 class="card-title">'.$row['name'].' '.$row['surname'].'</h2>
                    <p class="card-text">Description:</br>'.$row['player_description'].'</p>
                    <hr/>
                    <h6 class="card-title">Stats in 2020:</h6>
                    <p class="card-text">Total:'.$total.'</p>
                    <p class="card-text"><small class="text-muted">'.$rodo_info.'</small></p>';

        
        }
    }
    else{
        header('Location: /index.php');
    }
    $mysql_conn->close();
}
else{
    header('Location: /index.php');
}
?>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
