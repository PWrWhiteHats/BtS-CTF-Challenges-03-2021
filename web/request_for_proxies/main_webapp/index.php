<?php
	if (isset($_GET['address'])) {
            $address = $_GET['address'];
            if (str_contains($address, 'localhost') || str_contains($address, '127.0.0.1')) {
                echo $address . ' is forbidden';
            } else {
        		$curl_handle = curl_init();
                curl_setopt( $curl_handle, CURLOPT_URL, $address);
                curl_setopt( $curl_handle, CURLOPT_RETURNTRANSFER, true ); 
                curl_setopt( $curl_handle, CURLOPT_CONNECTTIMEOUT, 2 ); 
                curl_setopt($curl_handle, CURLOPT_FOLLOWLOCATION, true);
                $result = curl_exec( $curl_handle );
                curl_close( $curl_handle );
                echo $result;
            }

	} else {
            echo '<html>
                <head><title>My fancy proxy</title><link href="style.css" rel="stylesheet"></head>
                <body>';
            echo '<h1>Welcome to my new, fancy proxy!</h1>';
            echo '<p>It\'s created to help you bypass some stupid content restriction put over you by your school or employer. Just give me address of website and I\'m going to fetch it for you.';
    		echo '<form method="GET"><label for="fname">Address to fetch</label><br><input type="text" name="address" id="address"><input type="submit"></form></body>
                </html>';
	}
?>
