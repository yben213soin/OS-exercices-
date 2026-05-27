
# 1. OS Name and Kernel Version
echo -e "\033[1;32m[+] Operating System & Kernel Version:\033[0m"
if [ -f /etc/os-release ]; then
    # Dynamically source the exact distribution name (e.g., Ubuntu, Debian)
    source /etc/os-release
    echo "    Distribution: $NAME $VERSION"
else
    echo "    OS: $(uname -s)"
fi
echo "    Kernel Version: $(uname -r)"
echo "    Full Details: $(uname -a)"

echo "--------------------------------------------------"

# 2. Current Logged-in User
echo -e "\033[1;34m[+] Current Logged-in User:\033[0m"
echo "    Username: $(whoami)"

echo "--------------------------------------------------"

# 3. Current Working Directory
echo -e "\033[1;35m[+] Current Working Directory:\033[0m"
echo "    Path: $(pwd)"

echo "=================================================="
