def tools()-> list[object]:
    tools = [
    {
        "type": "function",
        "function": {
            "name": "user_account_balance",
            "description": "Get the last 4 digits from user to determine its account balance ,when a user asks or you as a assistant need to fetch the account balance.",
            "parameters": {
                "type": "object",
                "properties": {
                    "lastdigits:": {
                        "type": "string",
                        "description": "The user account number last 4 digits",
                    },
                },
                "required": ["lastdigits"],
                "additionalProperties": False,
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "last_transctions",
            "description": "Get the last 4 digits from user to determine its last transactions for example 'get my transactions'",
            "parameters": {
                "type": "object",
                "properties": {
                    "lastdigits_trans": {
                        "type": "string",
                        "description": "The user account number last 4 digits for transactions",
                    },
                },
                "required": ["lastdigits_trans"],
                "additionalProperties": False,
            },
        }
    },
        {
        "type": "function",
        "function": {
            "name": "check_usercard",
            "description": "Get the last 4 digits from user to suggest user a credit card 'apply for credit card'",
            "parameters": {
                "type": "object",
                "properties": {
                    "lastdigits_cards": {
                        "type": "string",
                        "description": "The user account number last 4 digits for suggesting credit card",
                    },
                },
                "required": ["lastdigits_cards"],
                "additionalProperties": False,
            },
        }
    }

    ]
    return tools