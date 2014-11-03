# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  config.vm.box = "ubuntu/precise32"
  
  # Note: if it complains about guest extension versions, you can manually install them
  # because each VirtualBox installation has the capability of mounting an ISO virtual
  # CD to install its guest extension from.

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. 
  config.vm.network :forwarded_port, guest: 3306, host: 3306

  config.vm.provision :shell, :path => "bootstrap.sh"

end