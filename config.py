PORT = 443

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00003200010567000090004000220001",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "dash.cloudflare.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
