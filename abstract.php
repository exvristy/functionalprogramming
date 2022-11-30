<?php

abstract class Laptop_Factory
{
    abstract function netbook();
    abstract function notebook();
}

class Asus_Factory extends Laptop_Factory
{
    function netbook()
    {
        return new Tipe_Netbook("Asus");
    }
    function notebook()
    {
        return new Tipe_Notebook("Asus");
    }
}

class Acer_Factory extends Laptop_Factory
{
    function netbook()
    {
        return new Tipe_Netbook("Acer");
    }
    function notebook()
    {
        return new Tipe_Notebook("Acer");
    }
}

abstract class Laptop_Tipe_Merk
{
    abstract function ambil_tipe();
    abstract function ambil_merk();
}

class Tipe_Netbook extends Laptop_Tipe_Merk
{
    public $merk;
    public $tipe = "Netbook";
    function __construct($merk) {
        $this->merk = $merk;
    }

    public function ambil_tipe()
    {
        return $this->tipe;
    }

    public function ambil_merk()
    {
        return $this->merk;
    }
}

class Tipe_Notebook extends Laptop_Tipe_Merk
{
    public $merk;
    public $tipe = "Notebook";
    function __construct($merk) {
        $this->merk = $merk;
    }

    public function ambil_tipe()
    {
        return $this->tipe;
    }

    public function ambil_merk()
    {
        return $this->merk;
    }
}

class Pilihan_Konsumen
{

    public static function Create_Laptop_Factory($factoryName)
    {
        switch($factoryName)
        {
            case "Acer" :
                return new Acer_Factory();
                break;
            case "Asus" :
                return new Asus_Factory();
                break;
        }
    }
}

class Tampilkan
{
	function __construct($nama_merk)
	{
		$fc = Pilihan_Konsumen::Create_Laptop_Factory($nama_merk);
		$netbook = $fc->netbook();
		$notebook = $fc->notebook();
		print_r($netbook);
		echo '<br>';
		print_r($notebook);
		echo '<br><br>';
	}
}

new Tampilkan("Asus");
new Tampilkan("Acer"); ?>
