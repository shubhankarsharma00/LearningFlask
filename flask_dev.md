Flask Development
--------------------

Documentation of the things I tried and what happened while trying to go from a
fresh Ubuntu Server AWS Instance to a full production-ready server with a
reddit-like app.

1. Create a new server on AWS, download the .pem file, modify security group to
   allow HTTP/HTTPS (port 80) and ssh.
   
2. Move .pem file to `~/.ssh/` and run `ssh-add path/file.pem` and then
   something like `eval $(ssh-agent -s)`.

3. Now we can ssh even without -i flag. Test it with `ssh ubuntu@ip.add.re.ss`.

4. To sync files and folders, install rsync on the local host. Syntax:
   `rsync -azP folder ubuntu@ip.add.re.ss:/home/ubuntu/`
   -a: 'archive' .. recursive + permissions etc
   -z: compress files
   -P: 'Progress' meters etc (is verbose)

5. (Optional) Add these to bash aliases to quickly run these commands.

6. Tried to use `lsyncd` for continuous sync. *Warning: it is very dangerous.*
   I destroyed one EC2 instance in trying to understand it. **DO NOT USE IT**.

7. I have decided to use python 3 and no venv's on the server. python3 is
   already installed, I tried to install pip but apt-get couldn't find
   python3-pip package. I did a `sudo apt-get update` and `upgrade`, it solved
   the issue. Now doing `sudo apt install python3-pip`.

8. Installed flask with `sudo pip install Flask`. Got a warning about old pip
   version so I ran `pip3 install --upgrade pip`. Now `pip` alone also works.

9. Made basic 'Hello World' app by
   following this [article](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
   to deploy app using apache. Note: first you will need to install the LAMP
   stack, link in the same article. I tried to symlink /var/www/FlaskApp to
   ~/code. Somehow after following all the steps in that article, the Flask app
   isn't working. The server is only showing "Index of /".

10. Trying to follow the same article on a clean ubuntu server VM. First had to
	set up network with two adapters - one host-only and one NAT. Found an answer
	on stackexchange about how to do that.
	Then followed exactly the steps in the article but still didn't work! WHY!?
	Let's ask on IRC...

11. Ahh! finally solved it! somehow disabling the default site seems to resolve
	the issue. `sudo a2dissite default` is the command.
   
12. Now trying to make it work again on the AWS server. Did the same things ...
	but mod_wsgi is using python2. Reconfiguring everying using python2 now.
	Finally got it to work on the development server!
