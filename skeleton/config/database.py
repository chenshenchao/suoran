connections = {
    "default": {
        "engine": "tortoise.backends.sqlite",
        "credentials": {
            "file_path": "common.db"
        }
    }
}

apps = {
    "default": {
        "models": [
            "model.visitor"
        ],
        "default_connection": "default"
    }
}
