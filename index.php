<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>PHP</title>
</head>

<body>
    <p>
        Thanks for visiting my website in this fine
        <?php
            $currentDate = date("l", strtotime($date)); 
            echo $currentDate;
        ?>.
    </p>
</body>

</html>