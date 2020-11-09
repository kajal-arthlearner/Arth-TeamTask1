import os
print("Welcome Abhishek")
while True:
  print("""Press 1 for aws configuration 
  Press 2 for hadoop installation 
      - uploading file
     - checking status 
Press 3 : For Exit""")
  ch = int(input("Enter Your Choice : "))
  if ch == 1:
    os.system("curl 'https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'")
    os.system("unzip awscliv2.zip")
    os.system("sudo ./aws/install")
    os.system("aws configure")
    while True:
      print("""Press 1: Create Key Pair for EC2
		    Press 2 : Security Group
		    Press 3 : Adding rule  to allow access to port 22 and 80 for the SG group Created
		    Press 4 : Launch EC2 instance with key and SG craeted above
                   """)
      awsch=int(input("Enter Your Choice : "))
      if awsch == 1:
        os.system("aws ec2 create-key-pair --key-name ArthCLI --query KeyMaterial --output text > ArthCLI.pem")
      elif awsch == 2:
        os.system("aws ec2 create-security-group --group-name Arthsg --description 'Abhishek security group' --vpc-id vpc-eb9ac183")
      elif awsch == 3:
        os.system("aws ec2 authorize-security-group-ingress --group-name Arthsg --protocol tcp --port 22 --cidr 0.0.0.0/0")
        os.system("aws ec2 authorize-security-group-ingress --group-name Arthsg --protocol tcp --port 80 --cidr 0.0.0.0/0")
      elif awsch == 4:
        os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --count 1 --instance-type t2.micro --key-name ArthCLI --security-groups Arthsg")
      x=input("Press Any Key to Continue or Q to quit AWS portal ")
      if x == "Q":
        exit()         
  elif ch == 2:
      os.system("pip3 install gdown")
      os.system("gdown   --id   16rNf8qrZ8Sg6NnC6YUd5vDUpOK27gSBJ    --output    hadoop.rpm")
      os.system("gdown   --id   1g5C4kznILCq4nsRovBCyDz58jLl-ghh3    --output    jdk.rpm")

      os.system("gdown   --id   1nWRYKKC0f4S8LNqNs7saW4kSxIMY0p4Y    --output   hdfsfile.xml")
      os.system("gdown   --id   1pagQjvfTQ5NxXmXxAfOEKjf1ZH5dIBOu    --output   corefile.xml")
      os.system("rpm -ivh jdk.rpm")
      os.system("rpm -ivh hadoop.rpm --force")
      while True:
        print("""Press 1 : Setup Hadoop NamedNode
      Press 2 : Start NamedNode
      Press 3 : Checking Status of NameNode
      Press 4 : Checking Hadoop Report
      Press 5 : For Exit""")
        hadoopch=int(input("Enter Your Choice : "))
        if hadoopch == 1:
         # os.system("mkdir /namednode")
          os.system("cp ./corefile.xml /etc/hadoop/core-site.xml")
          os.system("cp ./hdfsfile.xml /etc/hadoop/hdfs-site.xml")
          os.system("hadoop namenode -format")
        elif hadoopch == 2:
          os.system("hadoop-daemon.sh start namenode")
        elif hadoopch == 3:
          os.system("jps")
        elif hadoopch == 4:
          os.system("hadoop dfsadmin -report")
        elif hadoopch == 5:
          exit()
  elif ch == 3:
    exit()
  else:
    print("Wrong Input")
  input("Press any Key to Continue")
