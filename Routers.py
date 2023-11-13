routers ={
    "RBranch1" :
        {
            "Interface":
                {
                    "GigabitEthernet0/0":
                        {
                            "IP": "1.0.0.2 ",
                            "Mask": "255.0.0.0"
                        },
                    "GigabitEthernet0/1.1":
                        {
                            "IP": "192.168.1.33",
                            "Mask": "255.255.255.240"
                        },
                    "GigabitEthernet0/1.99":
                        {
                            "IP": "192.168.99.33",
                            "Mask": "255.255.255.240"
                        }
                }
        } ,
    "RBranch2" :
        {
            "Interface":
                {
                    "GigabitEthernet0/0":
                        {
                             "IP": "2.0.0.2",
                            "Mask" : "255.0.0.0"
                        },
                    "GigabitEthernet0/1.1":
                        {
                            "IP" : "192.168.1.17",
                            "Mask" : "255.255.255.240"

                        }, "GigabitEthernet0/1.99":
                        {
                            "IP" : "192.168.99.17",
                            "Mask" : "255.255.255.240"

                        }

                }
        },
    "R1Main":
        {
            "Interface":
                {
                    "GigabitEthernet0/0":
                        {
                            "IP": "3.0.0.2",
                            "Mask" : "255.0.0.0"
                        },
                    "GigabitEthernet0/1.1":
                        {
                            "IP": "192.168.1.1",
                            "Mask": "255.255.255.240"

                        }, "GigabitEthernet0/1.99":
                    {
                        "IP": "192.168.99.1",
                        "Mask": "255.255.255.240"

                    }

                }
        } ,
    "R2Main":
        {
            "Interface":
                {
                    "GigabitEthernet0/0":
                        {
                            "IP": "4.0.0.2",
                            "Mask" : "255.0.0.0"
                        },
                    "GigabitEthernet0/1.1":
                        {
                            "IP": "192.168.1.2",
                            "Mask": "255.255.255.240"

                        }, "GigabitEthernet0/1.99":
                    {
                        "IP": "192.168.99.2",
                        "Mask": "255.255.255.240"

                    }

                }
        }
}

