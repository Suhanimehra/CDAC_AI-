def traverse_nested_config(config_dict, path_str, default=None):
    if not isinstance(config_dict, dict) or not path_str:
        return default

    try:
        current = config_dict

        for key in path_str.split("."):
            current = current[key]

        return current

    except (KeyError, TypeError, AttributeError):
        return default


config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8080,
        "ssl": {
            "enabled": True,
            "cert_path": "/etc/ssl/certs"
        }
    },
    "database": "postgresql://localhost:5432"
}



print(traverse_nested_config(config, "server.ssl.cert_path"))
# /etc/ssl/certs


print(traverse_nested_config(config, "server.database.username", "guest"))
# guest


print(traverse_nested_config(config, "database.host", "localhost"))
# localhost
