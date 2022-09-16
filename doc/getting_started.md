## 1. Getting Started Guide  

### Dependencies

**packages and utilities used in this setup**  

_see Brewfile for the complete list_  

[colima](https://github.com/abiosoft/colima) • containerd runtime in linux virtual machine using hyperkit  
[nerdctl](https://github.com/containerd/nerdctl) • cli interface to containerd  
[minikube](https://github.com/kubernetes/minikube) • all-in-one local kubernetes, in dedicated virtual machine using docker   
[kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) • kubernetes api command-line tool  
[kubectx](https://github.com/ahmetb/kubectx) • cli to quickly swtich between local and remote k8s clusters  
[sonobuoy](https://github.com/vmware-tanzu/sonobuoy) • kubernetes conformance testing  
[kubefwd](https://github.com/txn2/kubefwd) • develop locally with remotes services available as they would be in the remote cluster  
[krew](https://github.com/kubernetes-sigs/krew/) kubectl plugin manager, mostly for cluster administrators   
(_some useful plugins_, e.g., `$ kubectl krew install konfig` )  
- _access-matrix_. Show an access matrix for server resources  
- _config-cleanup_. Automatically clean up your kubeconfig   
- _deprecations_. Compare a cluster against a specific version of k8s to reveal any deprecated uses  
- _evict-pod_. Evicts the given pod  
- _exec-as_. Like kubectl exec, but offers a `user` flag  
- _get-all_. Like 'kubectl get all', but everything  
- _images_. List detailed container information for a namespace  
- _konfig_. Merge and manage local kubeconfig  
- _mtail_. Tail logs from multiple pods matching label  
- _rbac-lookup_. Reverse lookup for RBAC  
- _rbac-view_. A tool to visualize your RBAC permissions  
- _resource-capacity_. Provides an overview of resource requests, limits, etc  
- _restart_. Restarts a pod with the given name  
- _roll_. Rolling delete or targted namespaces pods  
- _view-allocations_. Shows cluster cpu and memory allocations    
- _view-utilization_. Shows cluster cpu and memory utilization  
- _who-can_. like can-i but evaluates who at a permission level  
[helm](https://helm.sh) • manage kubernetes deployments  
[stern](https://github.com/wercker/stern)  • tails logs to the terminal from any number of local or remote pods  
[skaffold](https://github.com/GoogleContainerTools/skaffold) • continuous development on local kubernetes  
[kubeval](https://github.com/garethr/kubeval) • k8 yaml lint/inspection  

[mkcert](https://github.com/FiloSottile/mkcert) • Automated management of certificates and CA for local https  
[hostess](https://github.com/cbednarski/hostess) • /etc/hosts file manager for macos  

[terraform](https://www.terraform.io/downloads) • declarative infrastructure as code framework  
[terraform-docs](https://github.com/terraform-docs/terraform-docs) • generate documentation from Terraform modules  
[tflint](https://github.com/terraform-linters/tflint) • terraform linter
[hadolint](https://github.com/hadolint/hadolint) • Dockerfile lint/inspection  
[secrethub-cli](https://github.com/secrethub/secrethub-cli) • cli to secrethub apis (deprecating in favor of 1password)  
[opa](https://github.com/open-policy-agent/opa) • Open Policy Agent  
[awscli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) • aws api cli  
[aws-vault](https://github.com/99designs/aws-vault) • local aws crednetial management  
[chamber](https://github.com/segmentio/chamber) • cli for aws parameter store access   
[git-secrets](https://github.com/awslabs/git-secrets) 
[pyenv](https://github.com/pyenv/pyenv) • python version manager  
[rbenv](https://github.com/rbenv/rbenv) • ruby version manager  
[go](https://go.dev) • go programming language  
 
**building container images**  

Kubernetes requires that you use a runtime that conforms with at least v1alpha2 of the Container Runtime Interface (CRI). Containerd is (or soon will be) the default container runtime install used by most cloud provider managed kubernetes.  

There are a number of ways to build OCI compiant images. This project uses BuildKit and the local container runtime interface.  

Listed in the above packages is _colima_, a container runtime setup for MacOS. Once installed you can launch the virtual machine with containerd support and the nerdctl cli with the following commands:  
```bash
$ colima start --runtime containerd --cpu 2 --memory 6 --disk 20
$ colima nerdctl install
$ alias dr='nerdctl'      # add to your .zshrc if you want to use dr or docker or some other alias for nerdctl
```

Nerdctl is a Docker-compatible CLI for containerd.   

### helper scripts   

Throughout this guide you will also see references to some helper scripts. Python `invoke` and related task files in this repository provide a convenient way to install the various services and examples. Use `invoke -l` to see a list of available shortcuts.  

There is a Pipfile that can be used in setting up a local python virtual environment.  

In additional, the `tasks/install_mac.sh` script can be used to accelerate the installation process for these tools. Please review the script carefully before running on your system. Depends on the [homebrew](https://brew.sh) MacOS package manager.  

### Honorable mentions for additional local customization  

You may enjoy using these tools.  

[oh-my-zsh](https://ohmyz.sh)  
[kube-ps1](https://github.com/jonmosco/kube-ps1)  

<p align="center"><img width="800" alt="oh-my-zsh with kube-ps1" src="oh-my-zsh-capture.png"></p>

### Configuration for performing signed commits to GitHub

This explanation assumes MacOs and is based on using your personal KeyBase account.  

Use of Keybase is not a requirement for signed commits and there are many posts you can find that describe alternative means. Many people already use other popular keyservers (e.g., pgp.mit.edu, keyserver.ubuntu.com)

Requirements:
* Github account
* Keybase account
* GPG service locally

```bash
$ brew cask install keybase  # typically already installed as part of keybase app install
$ brew install gpg
```

Create new personal key. (Note: you can skip if you already maintain your key via alternative means)
```bash
$ keybase pgp gen --multi

# If your gpg is running local then you should see the following

Enter your real name, which will be publicly visible in your new key: Jane Doe
Enter a public email address for your key: jdoe@thoughtworks.com
Enter another email address (or <enter> when done): jane.doe@gmail.com
Enter another email address (or <enter> when done):
Push an encrypted copy of your new secret key to the Keybase.io server? [Y/n] Y
When exporting to the GnuPG keychain, encrypt private keys with a passphrase? [Y/n] Y
▶ INFO PGP User ID: Jane Doe <jdoe@thoughtworks.com> [primary]
▶ INFO PGP User ID: Jane Doe <jane.doe@gmail.com>
▶ INFO Generating primary key (4096 bits)
▶ INFO Generating encryption subkey (4096 bits)
▶ INFO Generated new PGP key:
▶ INFO   user: Jane Doe <jdoe@thoughtworks.com>
▶ INFO   4096-bit RSA key, ID 5BE03B7DE63C0271, created 2020-05-25
▶ INFO Exported new key to the local GPG keychain
```

List info needed to setup git locally

```bash
$ gpg --list-secret-keys --keyid-format LONG
/Users/ncheneweth/.gnupg/pubring.kbx
------------------------------------
sec   rsa4096/A8E47CAE38308EC9 2020-05-25 [SC] [expires: 2036-05-21]
      7703E0D1ECF17C64C6B09DDFA8E47CAE38308EC9
uid                 [ unknown] Jane Doe <jdoe@thoughtworks.com>
uid                 [ unknown] Jane Doe <njane.doe@gmail.com>
```

# add to git config

```bash
$ git config --global user.signingkey A8E47CAE38308EC9
$ git config --global commit.gpgsign true
```

# copy to clipboard for pasting into github
```bash
keybase pgp export -q 5BE03B7DE63C0271 | pbcopy
```

# test
```bash
export GPG_TTY=$(tty)
echo "test" | gpg --clearsign
```

# Set as default gpg key
```bash
$ $EDITOR ~/.gnupg/gpg.conf
```

# Add line:

```bash
default-key 5BE03B7DE63C0271
```
There are couple different common ways of getting your local config to know to use the key for signing every time. 

```bash
$ brew uninstall pinentry-mac
```

Some people find that pinentry installed with brew does not allow the password to be saved to macOS's keychain.
If you do not see "Save in Keychain" after following Method 1, try the GPG Suite versions, available from gpgtools.org, or from brew by running:

```bash
$ brew install gpg-suite --cask
```

Once installed, open Spotlight and search for "GPGPreferences", or open system preferences and select "GPGPreferences." Select the Default Key if it is not already selected, and ensure "Store in OS X Keychain" is checked.

## working with multiple SSH keys

If you need to maintain multiple SSH and GPG signing keys, below is one strategy:  

Edit your ~/.ssh/config file:  

```bash
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes

Host github.com-company-1
  HostName github.com
  User git
  IdentityFile ~/.ssh/company_1_id_rsa
  IdentitiesOnly yes
  
Host bitbucket.org-company-2
  HostName bitbucket.org
  User git
  IdentityFile ~/.ssh/company_2_id_rsa
  IdentitiesOnly yes

Host *
  AddKeysToAgent yes
  IdentitiesOnly yes
  PreferredAuthentications publickey
  UseKeychain yes
  Compression yes
```

Edit your ~/.gitconfig file
```bash
[init]
  defaultBranch = main

[commit]
  gpgsign = true

# ...

[user]
  name = Jane Doe
  useConfigOnly = true

# optional (if you organize your repositories by ssh context)  

[include]
  path = ~/.gitconfig-default

[includeIf "gitdir:~/github/company-1/"]
  path = ~/.gitconfig-company-1

[includeIf "gitdir:~/github/company-2/"]
  path = ~/.gitconfig-company-2
 ```
 
 For each of the config specific files:  
 
 ~/.gitconfig-default  
 ```bash
 [user]
	   email = jdoe@thoughtworks.com
	   signingkey = 5BE03B7DE63C0271
 ```
 
  ~/.gitconfig-company-1  
 ```bash
 [user]
	  email = jdoe@company-1.com
	  signingkey = 6F3B53E64B964B824

[url "git@github.com-company-1"]
	  insteadOf = git@github.com
 ```
 
   ~/.gitconfig-company-2  
 ```bash
  [user]
	  email = jdoe@company-2.com
	  signingkey = 3456753E64B964B824

[url "git@bitbucket.org-company-2"]
	  insteadOf = git@github.com
 ```
 
[Return](../README.md)
