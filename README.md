# Getting Started

    $ git clone https://github.com/sashawins/calculator-pipeline.git
    $ cd calculator-pipeline

    $ docker build -t myjenkins .
    $ docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 --name jenkins-alpine myjenkins

## Launching Jenkins

**Using** `http://localhost:8080` or `http://0.0.0.0:8080` on your host machine browser.  
**Login** via `admin` as a login and `%/var/lib/jenkins/secrets/initialAdminPassword%` as a password.

## Creating Pipeline

**Via** creating new item named `CalculatorMicroservice` as a **Multibranch Pipeline** and saving it with default settings.

## Configurung Pipeline

Add your credentials choosing **Username with password** kind containing login and password from your _GitHub_ using **Credentials tab inside your Multibranch Pipeline job**, so it could be scoped to our Job only.  
Go back to configuring our pipeline. On **Branch Sources** tab click **Add** and choose **Git**. Insert `https://github.com/sashawins/calculator-pipeline.git` as a **Project Repository** and your _GitHub_ username with password as **Credentials**.

# Start Building

On your Job's workspace choose **Scan Multibranch Pipeline Log** and then **Multibranch Pipeline Events**.  
It should now start a build which will appear in **Build Queue**.
