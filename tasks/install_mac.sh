
#!/bin/bash
set -e

if ! command -v brew &> /dev/null
then
    echo "Installing homebrew"
    curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh
fi

echo "Homebrew installed. Running brew bundle"
brew bundle -v

echo "Installing kubectl plugins"
kubectl krew install konfig
echo "All done! Be sure to export PATH=$PATH:$HOME/.krew/bin to your rc file"
