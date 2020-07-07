# ansible_ec2_python

## Description:
The goal is to create an EC2 machine using ansible playbook and install dependecy using two roles for running a python script that will list all the instance type for an AWS account 

## Pre-Requisite
 - Must have an access and secret key to run playbook and python script
 - Should have key pair and security group created
 - ansible and boto3 should be installed where playbook is going to run

## Installtion

The following are installtion for Ubuntu server for running ansible playbook
```sh
$ sudo apt update
$ sudo apt install software-properties-common
```
Install Python and Boto3
```sh
$ sudo apt install python
$ sudo apt install python-pip
$ sudo pip install boto3
```
Install Ansible
```sh
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt update
$ sudo apt install ansible
```

## Configuration
1. Clone the code
```sh
$ git clone https://github.com/prasithtoughboy/ansible_ec2_python.git
```
2. Go inside the path
```sh
$ cd ~/ansible_ec2_python
```
3. Change the values for **aws_access_key**, **aws_secret_key**, **key_name** and **security_group** in the vars file of ec2-launch according to your input
```sh
$ vi  ec2-launch/vars/main.yml
```
4. Copy the created key-pair in EC2 to any path say /opt/test.pem and provide permission ``` chmod 400 /opt/test.pem``` and add path entry like below in /etc/ansible/ansible.cfg to take SSH for the newly created instance and install it's dependecies
```sh
vi /etc/ansible/ansible.cfg

[defaults]
host_key_checking = False
private_key_file = /opt/test.pem
```
## Run
Now run the playbook after configuring your inputs
```sh
ansible-playbook roles.yaml
```
**You will see an EC2 machine created after successful completion of playbook**

Login to the machine using the SSH connection string for EC2 in the console using your created key file.
After login goto opt directoy and run the python file
```sh
$ cd /opt
$ python list_ec2_types.py
$ python list_ec2_types.py 't2.micro'
```
