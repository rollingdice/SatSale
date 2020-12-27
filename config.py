# Bitcoin node connection settings
host = "127.0.0.1"
rpcport = "8332"
username = "bitcoinrpc"
password = "RPAPASSWORD"

# SSH tunnel to node (raspberry pi!)
# Make sure this command works `ssh HOST@IP -q -N -L 8332:localhost:8332`
tunnel_host = "HOST@IP"

# Check for payment every xx seconds
pollrate = 15

# Payment expires after xx seconds
payment_timeout = 60*60

# Required confirmations for a payment
required_confirmations = 2

# Global connection attempts
connection_attempts = 3