itenary_schema = {
    "type": "object",
    "properties": {
        "guests": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "passport": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
                    "family": {"type": "string"},
                },
                "required": ["name", "passport"],
            },
        },
        "itenary": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "format": "date"},
                    "from": {"type": "string"},
                    "to": {"type": "string"},
                },
                "required": ["date", "from", "to"],
            },
        },
    },
    "required": ["guests", "itenary"],
}


visa_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "passport": {"type": "string"},
        "purpose": {"type": "string"},
        "guest_country": {"type": "string"},
    },
    "required": ["name", "passport", "purpose","guest_country"],
}

undertaking_single_schema = {
    "type": "object",
    "properties": {"name": {"type": "string"}},
    "required": ["name"],
}

undertaking_family_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "array": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "sl": {"type": "string"},
                    "name": {"type": "string"},
                    "number": {"type": "string"},
                    "remarks": {"type": "string"},
                },
                "required": ["sl", "name", "number", "remarks"],
            },
        },
    },
    "required": ["name", "array"],
}

authorize_schema = {
    "type": "object",
    "properties": {
        "client": {"type": "string"},
        "client_passport_number": {"type": "string"},
        "authorizer": {"type": "string"},
        "relationship": {"type": "string"},
        "authorizer_passport_number": {"type": "string"},
        "contact": {"type": "string"},
        "name_ava": {"type": "string"},
        "address_ava": {"type": "string"},
    },
    "required": [
        "client",
        "client_passport_number",
        "authorizer",
        "relationship",
        "authorizer_passport_number",
        "contact",
        "name_ava",
        "address_ava",
    ],
}
