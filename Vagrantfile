Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"

  config.vm.provider "virtualbox" do |v|
    v.name = "Python-DevEnv"
    v.memory = 4096
  end

  config.vm.provision :shell, path: "provisionning.sh"
end
